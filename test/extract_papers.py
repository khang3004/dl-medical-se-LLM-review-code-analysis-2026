import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


from src.papers_extractor import *
file_part_1 = "/Users/KhangDS/Library/CloudStorage/GoogleDrive-gausseuler159357@gmail.com/My Drive/Static_Data/HCMUS_documents/Course_docs/Introduction2Dataa_Science/ICCCI_2025_part1.pdf"  # Usually Part I
file_part_2 = "/Users/KhangDS/Library/CloudStorage/GoogleDrive-gausseuler159357@gmail.com/My Drive/Static_Data/HCMUS_documents/Course_docs/Introduction2Dataa_Science/ICCCI_2025_part2.pdf"  # Part II

# Initialize extractors
try:
    extractor_p1 = PDFExtractor(file_part_1)
    extractor_p2 = PDFExtractor(file_part_2)

    def extract_paper_smart(title_query, output_name):
        print(f"\n--- Processing: {title_query} ---")
        # Try Part 1 first
        if extractor_p1.find_and_extract_by_title(title_query, output_name):
            return
        # If not found, try Part 2
        print(f"Title not found in Part 1, checking Part 2...")
        if extractor_p2.find_and_extract_by_title(title_query, output_name):
            return
        
        print(f"[ERROR] Could not find paper '{title_query}' in either file.")

    # 1. Leukemia Detection
    extract_paper_smart("Leukemia Detection Based on YOLOv11", "docs/Leukemia_Detection.pdf")

    # 2. Alzheimer's Disease
    extract_paper_smart("The New method for detection of Alzheimer", "docs/detection_of_Alzheimer_Disease.pdf")

    # 3. LLMs as Code Review Agents
    extract_paper_smart("LLMs as Code Review Agents", "docs/LLMs_as_Code_Review_Agents_Review.pdf")

except Exception as e:
    print(f"[ERROR] An unexpected error occurred: {e}")
    import traceback
    traceback.print_exc()