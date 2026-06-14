import os
from pypdf import PdfReader

docs_dir = "/Users/KhangDS/Programing/HCMUS_Code/Introduction2DS/docs"
pdf_files = [f for f in os.listdir(docs_dir) if f.endswith(".pdf")]

print("Found PDF files:", pdf_files)

for pdf_file in pdf_files:
    path = os.path.join(docs_dir, pdf_file)
    print(f"\n==================================================")
    print(f"File: {pdf_file}")
    print(f"==================================================")
    reader = PdfReader(path)
    print(f"Total pages: {len(reader.pages)}")
    
    # Print the first 2 pages (Abstract + Introduction)
    for i in range(min(2, len(reader.pages))):
        print(f"\n--- Page {i+1} ---")
        text = reader.pages[i].extract_text()
        print(text[:1500]) # first 1500 chars of each page
