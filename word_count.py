import os
import re
from bs4 import BeautifulSoup
from openpyxl import Workbook
from openpyxl.styles import Font

def extract_visible_text(markdown_text):
    """
    Extracts all visible text (like what Word sees when pasted).
    Removes markup but keeps all readable content.
    """
    # Parse HTML-like Markdown safely
    soup = BeautifulSoup(markdown_text, "html.parser")

    # Remove scripts, styles, and code — Word ignores these
    for tag in soup(["script", "style", "code"]):
        tag.decompose()

    # Extract visible text
    text = soup.get_text(separator=" ", strip=True)

    # Clean excessive whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def word_count_like_word(text):
    """
    Count words following Microsoft Word's logic.
    """
    # Word’s algorithm treats these as one word each:
    # - hyphenated compounds
    # - numbers with decimals or commas
    # - URLs / emails
    pattern = re.compile(
        r"""
        [A-Za-zÀ-ÖØ-öø-ÿ]+(?:[-'][A-Za-zÀ-ÖØ-öø-ÿ]+)*  # words with hyphens or apostrophes
        | \d+(?:[.,]\d+)*                              # numbers like 3.14 or 1,000
        | [A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,} # emails
        | https?://\S+                                  # URLs
        """,
        re.VERBOSE
    )
    return len(pattern.findall(text))


def count_words_in_markdown(folder_path="."):
    """
    Recursively count words in all Markdown (.md) files,
    following Microsoft Word's word count definition.
    """
    total_words = 0
    file_word_counts = {}

    for root, _, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".md"):
                path = os.path.join(root, filename)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()
                except Exception as e:
                    print(f"⚠️ Could not read {path}: {e}")
                    continue

                text = extract_visible_text(content)
                count = word_count_like_word(text)

                relative_path = os.path.relpath(path, folder_path)
                file_word_counts[relative_path] = count
                total_words += count

    return total_words, file_word_counts


def save_to_excel(file_word_counts, total_words, output_file="word_count_report.xlsx"):
    """
    Save word counts to Excel in a readable format.
    """
    wb = Workbook()
    ws = wb.active
    ws.title = "Word Count Report"

    # Header row
    ws.append(["Folder", "File Name", "Word Count"])
    header_font = Font(bold=True)
    for cell in ws[1]:
        cell.font = header_font

    # Data rows
    for path, count in sorted(file_word_counts.items()):
        folder, file_name = os.path.split(path)
        ws.append([folder, file_name, count])

    # Total row
    ws.append(["", "TOTAL", total_words])
    ws.cell(ws.max_row, 2).font = Font(bold=True)
    ws.cell(ws.max_row, 3).font = Font(bold=True)

    # Auto column width
    for col in ws.columns:
        max_len = max(len(str(cell.value or "")) for cell in col)
        ws.column_dimensions[col[0].column_letter].width = max_len + 2

    wb.save(output_file)
    print(f"\n✅ Word count report saved as: {output_file}")


if __name__ == "__main__":
    folder = "."
    total, counts = count_words_in_markdown(folder)

    print("Word count by file:")
    for file, wc in sorted(counts.items()):
        print(f"  {file}: {wc} words")

    print(f"\nTotal word count (Microsoft Word equivalent): {total}")
    save_to_excel(counts, total)
