import os
import re
from bs4 import BeautifulSoup
from openpyxl import Workbook
from openpyxl.styles import Font

def clean_markdown_syntax(text):
    """
    Strip Markdown-specific syntax that would not appear as text in Word.
    """
    # Remove Markdown tables and formatting
    text = re.sub(r'^\|.*\|\s*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)  # images
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)  # links keep label only
    text = re.sub(r'[#>*_`~\-]+', '', text)  # headers, bold, italics, etc.
    return text

def extract_visible_text(content, is_html=False):
    """
    Extract visible text like Word would see:
    - For HTML, remove tags but keep displayed text
    - For Markdown, strip markup and convert inline HTML if present
    """
    if is_html:
        soup = BeautifulSoup(content, "html.parser")
        # Remove hidden or non-textual elements
        for tag in soup(["script", "style", "code", "noscript", "meta", "link"]):
            tag.decompose()
        text = soup.get_text(separator=" ", strip=True)
    else:
        # Markdown may contain HTML fragments — parse and clean
        content = clean_markdown_syntax(content)
        soup = BeautifulSoup(content, "html.parser")
        for tag in soup(["script", "style", "code", "noscript", "meta", "link"]):
            tag.decompose()
        text = soup.get_text(separator=" ", strip=True)

    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def word_count_like_word(text):
    """
    Count words following Microsoft Word's definition.
    """
    pattern = re.compile(
        r"""
        [A-Za-zÀ-ÖØ-öø-ÿ]+(?:[-'][A-Za-zÀ-ÖØ-öø-ÿ]+)*  # Hyphenated or apostrophized words
        | \d+(?:[.,]\d+)*                              # Numbers like 3.14 or 1,000
        | [A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,} # Emails
        | https?://\S+                                  # URLs
        """,
        re.VERBOSE
    )
    return len(pattern.findall(text))

def count_words(folder_path="."):
    """
    Recursively count words in .md and .html/.htm files using Word rules.
    """
    total_words = 0
    file_word_counts = {}

    for root, _, files in os.walk(folder_path):
        for filename in files:
            ext = os.path.splitext(filename.lower())[1]
            if ext in [".md", ".html", ".htm"]:
                path = os.path.join(root, filename)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()
                except Exception as e:
                    print(f"⚠️ Could not read {path}: {e}")
                    continue

                is_html = ext in [".html", ".htm"]
                text = extract_visible_text(content, is_html=is_html)
                count = word_count_like_word(text)

                relative_path = os.path.relpath(path, folder_path)
                file_word_counts[relative_path] = count
                total_words += count

    return total_words, file_word_counts

def save_to_excel(file_word_counts, total_words, output_file="word_count_report.xlsx"):
    """
    Save the word counts to an Excel file.
    """
    wb = Workbook()
    ws = wb.active
    ws.title = "Word Count Report"

    ws.append(["Folder", "File Name", "Word Count"])
    for cell in ws[1]:
        cell.font = Font(bold=True)

    for path, count in sorted(file_word_counts.items()):
        folder, file_name = os.path.split(path)
        ws.append([folder, file_name, count])

    ws.append(["", "TOTAL", total_words])
    ws.cell(ws.max_row, 2).font = Font(bold=True)
    ws.cell(ws.max_row, 3).font = Font(bold=True)

    for col in ws.columns:
        max_len = max(len(str(cell.value or "")) for cell in col)
        ws.column_dimensions[col[0].column_letter].width = max_len + 2

    wb.save(output_file)
    print(f"\n✅ Word count report saved as: {output_file}")

if __name__ == "__main__":
    folder = "."
    total, counts = count_words(folder)

    print("Word count by file:")
    for file, wc in sorted(counts.items()):
        print(f"  {file}: {wc} words")

    print(f"\nTotal word count (Microsoft Word equivalent): {total}")
    save_to_excel(counts, total)
