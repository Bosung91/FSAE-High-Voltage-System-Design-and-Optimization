import os
import re
from bs4 import BeautifulSoup
from openpyxl import Workbook
from openpyxl.styles import Font

# === CONFIGURATION ===
TARGET_FOLDER = "FSAE-High-Voltage-System-Design-and-Optimization"
EXCLUDED_FILE = "appendix.md"
OUTPUT_FILE = "word_count_report.xlsx"


def clean_markdown_syntax(text):
    """
    Strip Markdown formatting while keeping visible text (like Word would see).
    """
    text = re.sub(r'^\|.*\|\s*$', '', text, flags=re.MULTILINE)  # tables
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)  # images
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)  # links: keep label only
    text = re.sub(r'[`*_#>\-~]+', '', text)  # markdown formatting symbols
    return text


def extract_visible_text(content):
    """
    Extract visible text from Markdown, removing hidden markup and HTML tags.
    """
    # Clean markdown markup
    content = clean_markdown_syntax(content)

    # Parse embedded HTML safely
    soup = BeautifulSoup(content, "html.parser")

    # Remove non-visible or code tags
    for tag in soup(["script", "style", "code", "noscript", "meta", "link"]):
        tag.decompose()

    # Get visible text
    text = soup.get_text(separator=" ", strip=True)

    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def word_count_like_word(text):
    """
    Count words using Microsoft Word-style rules.
    """
    pattern = re.compile(
        r"""
        [A-Za-zÀ-ÖØ-öø-ÿ]+(?:[-'][A-Za-zÀ-ÖØ-öø-ÿ]+)*  # Hyphenated words
        | \d+(?:[.,]\d+)*                              # Numbers with commas/decimals
        | [A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,} # Emails
        | https?://\S+                                  # URLs
        """,
        re.VERBOSE
    )
    return len(pattern.findall(text))


def count_words_in_markdown(folder_path):
    """
    Count words in all Markdown (.md) files inside the folder (recursively),
    excluding 'appendix.md', using Microsoft Word logic.
    """
    total_words = 0
    file_word_counts = {}

    for root, _, files in os.walk(folder_path):
        for filename in files:
            if filename.lower().endswith(".md") and filename.lower() != EXCLUDED_FILE:
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


def save_to_excel(file_word_counts, total_words, output_file):
    """
    Save the word counts to an Excel file.
    """
    wb = Workbook()
    ws = wb.active
    ws.title = "Word Count Report"

    # Headers
    ws.append(["Folder", "File Name", "Word Count"])
    for cell in ws[1]:
        cell.font = Font(bold=True)

    # Data
    for path, count in sorted(file_word_counts.items()):
        folder, file_name = os.path.split(path)
        ws.append([folder, file_name, count])

    # Total
    ws.append(["", "TOTAL (excluding appendix.md)", total_words])
    ws.cell(ws.max_row, 2).font = Font(bold=True)
    ws.cell(ws.max_row, 3).font = Font(bold=True)

    # Auto column width
    for col in ws.columns:
        max_len = max(len(str(cell.value or "")) for cell in col)
        ws.column_dimensions[col[0].column_letter].width = max_len + 2

    wb.save(output_file)
    print(f"\n✅ Word count report saved as: {output_file}")


if __name__ == "__main__":
    if not os.path.exists(TARGET_FOLDER):
        print(f"❌ Folder not found: {TARGET_FOLDER}")
    else:
        total, counts = count_words_in_markdown(TARGET_FOLDER)

        print("Word count by file:")
        for file, wc in sorted(counts.items()):
            print(f"  {file}: {wc} words")

        print(f"\nTotal (excluding appendix.md): {total}")
        save_to_excel(counts, total, OUTPUT_FILE)
