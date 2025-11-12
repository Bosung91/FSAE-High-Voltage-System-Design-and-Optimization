import re
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from openpyxl.styles import Font


def fetch_webpage_text(url, exclude_tables=True):
    """
    Fetch webpage and extract visible text (excluding hidden elements).
    If exclude_tables=True, text inside <table> tags is removed.
    """
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
    except Exception as e:
        print(f"❌ Error fetching {url}: {e}")
        return ""

    soup = BeautifulSoup(response.text, "html.parser")

    # Remove invisible or irrelevant elements
    for tag in soup(["script", "style", "noscript", "meta", "link", "header", "footer", "nav", "form"]):
        tag.decompose()

    # Optionally remove tables
    if exclude_tables:
        for table in soup.find_all("table"):
            table.decompose()

    # Extract visible text
    text = soup.get_text(separator=" ", strip=True)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def word_count_like_word(text):
    """
    Count words using Microsoft Word's logic.
    """
    pattern = re.compile(
        r"""
        [A-Za-zÀ-ÖØ-öø-ÿ]+(?:[-'][A-Za-zÀ-ÖØ-öø-ÿ]+)*   # Hyphenated or apostrophized words
        | \d+(?:[.,]\d+)*                               # Numbers with commas/decimals
        | [A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,} # Emails
        | https?://\S+                                   # URLs
        """,
        re.VERBOSE,
    )
    return len(pattern.findall(text))


def analyze_webpages(urls, exclude_tables=True):
    """
    Process multiple webpages and return detailed word count results.
    """
    results = []
    total = 0

    for url in urls:
        text = fetch_webpage_text(url, exclude_tables=exclude_tables)
        count = word_count_like_word(text)
        total += count

        results.append({
            "url": url,
            "characters": len(text),
            "word_count": count
        })

        print(f"🔗 {url}")
        print(f"🧾 Visible text length: {len(text):,} characters")
        print(f"🧮 Word count (Word-style): {count:,} words\n")

    print(f"✅ Combined total: {total:,} words")
    return results, total


def save_results_to_excel(results, total, output_file="webpage_word_count.xlsx"):
    """
    Save the webpage analysis results to an Excel file.
    """
    wb = Workbook()
    ws = wb.active
    ws.title = "Webpage Word Count"

    # Headers
    ws.append(["URL", "Visible Characters", "Word Count"])
    for cell in ws[1]:
        cell.font = Font(bold=True)

    # Data rows
    for r in results:
        ws.append([r["url"], r["characters"], r["word_count"]])

    # Total row
    ws.append(["TOTAL", "", total])
    ws.cell(ws.max_row, 1).font = Font(bold=True)
    ws.cell(ws.max_row, 3).font = Font(bold=True)

    # Auto column width
    for col in ws.columns:
        max_len = max(len(str(cell.value or "")) for cell in col)
        ws.column_dimensions[col[0].column_letter].width = max_len + 2

    wb.save(output_file)
    print(f"\n📊 Results saved to: {output_file}")


if __name__ == "__main__":
    # 🧠 Example usage: list of target URLs
    urls = [
        'https://bosung91.github.io/FSAE-High-Voltage-System-Design-and-Optimization/',
        'https://bosung91.github.io/FSAE-High-Voltage-System-Design-and-Optimization/introduction.html',
        'https://bosung91.github.io/FSAE-High-Voltage-System-Design-and-Optimization/objective-and-scope.html',
        'https://bosung91.github.io/FSAE-High-Voltage-System-Design-and-Optimization/context-of-problem.html',
        'https://bosung91.github.io/FSAE-High-Voltage-System-Design-and-Optimization/R25evo/r25evo.html',
        'https://bosung91.github.io/FSAE-High-Voltage-System-Design-and-Optimization/R26e/precharge-discharge-pcb.html',
        'https://bosung91.github.io/FSAE-High-Voltage-System-Design-and-Optimization/R26e/tractive-battery-pdm.html',
        'https://bosung91.github.io/FSAE-High-Voltage-System-Design-and-Optimization/R26e/hv-distribution-pcb.html',
        'https://bosung91.github.io/FSAE-High-Voltage-System-Design-and-Optimization/shortcomings.html',
        'https://bosung91.github.io/FSAE-High-Voltage-System-Design-and-Optimization/future-work.html',
        'https://bosung91.github.io/FSAE-High-Voltage-System-Design-and-Optimization/references.html'
    ]

    results, total = analyze_webpages(urls, exclude_tables=True)
    save_results_to_excel(results, total)
