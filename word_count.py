import os
import re
from openpyxl import Workbook
from openpyxl.styles import Font

def clean_markdown(text):
    """
    Remove Markdown tables, hyperlinks, and formatting.
    """
    # Remove tables (lines starting and ending with |)
    text = re.sub(r'^\|.*\|\s*$', '', text, flags=re.MULTILINE)

    # Remove inline links: [text](url)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', '', text)

    # Remove reference-style links: [text][id] or [id]: url
    text = re.sub(r'\[([^\]]+)\]\[[^\]]*\]', '', text)
    text = re.sub(r'^\s*\[[^\]]+\]:\s*\S+\s*$', '', text, flags=re.MULTILINE)

    # Remove images ![alt](url)
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)

    # Remove Markdown formatting symbols (*, #, >, etc.)
    text = re.sub(r'[#>*_`~\-]+', '', text)

    return text


def count_words_in_markdown(folder_path="."):
    """
    Recursively count words in all Markdown (.md) files within a folder,
    excluding tables and hyperlinks.
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

                clean_text = clean_markdown(content)
                words = re.findall(r'\b\w+\b', clean_text)
                count = len(words)
                relative_path = os.path.relpath(path, folder_path)
                file_word_counts[relative_path] = count
                total_words += count

    return total_words, file_word_counts


def save_to_excel(file_word_counts, total_words, output_file="word_count_report.xlsx"):
    """
    Save the word counts to an Excel file with formatting.
    """
    wb = Workbook()
    ws = wb.active
    ws.title = "Word Count Report"

    # Headers
    ws.append(["Folder", "File Name", "Word Count"])
    header_font = Font(bold=True)
    for cell in ws[1]:
        cell.font = header_font

    # Add data
    for path, count in sorted(file_word_counts.items()):
        folder, file_name = os.path.split(path)
        ws.append([folder, file_name, count])

    # Add total row
    ws.append(["", "TOTAL", total_words])
    ws.cell(ws.max_row, 2).font = Font(bold=True)
    ws.cell(ws.max_row, 3).font = Font(bold=True)

    # Auto-adjust column widths
    for col in ws.columns:
        max_length = 0
        col_letter = col[0].column_letter
        for cell in col:
            if cell.value:
                max_length = max(max_length, len(str(cell.value)))
        ws.column_dimensions[col_letter].width = max_length + 2

    wb.save(output_file)
    print(f"\n✅ Word count report saved as: {output_file}")


if __name__ == "__main__":
    folder = "."
    total, counts = count_words_in_markdown(folder)

    print("Word count by file:")
    for file, wc in sorted(counts.items()):
        print(f"  {file}: {wc} words")

    print(f"\nTotal word count (excluding tables and hyperlinks): {total}")
    save_to_excel(counts, total)
