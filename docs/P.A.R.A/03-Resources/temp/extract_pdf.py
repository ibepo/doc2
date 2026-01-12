#!/usr/bin/env python3
"""Extract comprehensive information from 2026 Steel Market Outlook PDF"""

import pdfplumber
import json
import re
from pathlib import Path

pdf_path = "/Users/ibepo/Documents/GitHub/doc2/docs/P.A.R.A/01-Projects/ts/2026年钢铁市场与行业展望(终版)(4).pdf"
output_dir = "/Users/ibepo/Documents/GitHub/doc2/docs/P.A.R.A/03-Resources/temp"
Path(output_dir).mkdir(parents=True, exist_ok=True)

print("=" * 80)
print("PDF BASIC INFO")
print("=" * 80)

with pdfplumber.open(pdf_path) as pdf:
    print(f"Total Pages: {len(pdf.pages)}")

metadata_output = {"total_pages": len(pdf.pages), "source": pdf_path}

with open(f"{output_dir}/metadata.json", "w", encoding="utf-8") as f:
    json.dump(metadata_output, f, ensure_ascii=False, indent=2)

# Extract full text with pdfplumber
print("\n" + "=" * 80)
print("TEXT EXTRACTION")
print("=" * 80)

full_text = ""
page_texts = []

with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages, 1):
        print(f"\n--- Page {i} ---")
        text = page.extract_text()
        page_texts.append({"page": i, "text": text})
        full_text += f"\n\n{'=' * 80}\nPage {i}\n{'=' * 80}\n{text}"

# Save full text
with open(f"{output_dir}/full_text.txt", "w", encoding="utf-8") as f:
    f.write(full_text)

# Save page-by-page JSON
with open(f"{output_dir}/page_texts.json", "w", encoding="utf-8") as f:
    json.dump(page_texts, f, ensure_ascii=False, indent=2)

# Extract tables
print("\n" + "=" * 80)
print("TABLE EXTRACTION")
print("=" * 80)

all_tables = []

with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages, 1):
        tables = page.extract_tables()
        if tables:
            print(f"\n--- Page {i}: {len(tables)} table(s) found ---")
            for j, table in enumerate(tables):
                print(f"\nTable {j + 1}:")
                all_tables.append({"page": i, "table_num": j + 1, "data": table})
                for row in table:
                    print(row)

# Save tables
with open(f"{output_dir}/tables.json", "w", encoding="utf-8") as f:
    json.dump(all_tables, f, ensure_ascii=False, indent=2)

print(f"\n\nExtraction complete!")
print(f"- Metadata saved to: {output_dir}/metadata.json")
print(f"- Full text saved to: {output_dir}/full_text.txt")
print(f"- Page texts saved to: {output_dir}/page_texts.json")
print(f"- Tables saved to: {output_dir}/tables.json")
