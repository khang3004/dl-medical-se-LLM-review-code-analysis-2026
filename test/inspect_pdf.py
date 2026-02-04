
import sys
from pathlib import Path

# Thêm thư mục gốc vào Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from pypdf import PdfReader

file_part_1 = "/Users/KhangDS/Library/CloudStorage/GoogleDrive-gausseuler159357@gmail.com/My Drive/Static_Data/HCMUS_documents/Course_docs/Introduction2Dataa_Science/ICCCI_2025_part1.pdf"
file_part_2 = "/Users/KhangDS/Library/CloudStorage/GoogleDrive-gausseuler159357@gmail.com/My Drive/Static_Data/HCMUS_documents/Course_docs/Introduction2Dataa_Science/ICCCI_2025_part2.pdf"

def inspect_outline(file_path):
    print(f"--- Inspecting: {Path(file_path).name} ---")
    try:
        reader = PdfReader(file_path)
        if not reader.outline:
            print("No outline found.")
            return

        print(f"Outline found with {len(reader.outline)} items.")
        
        # Print first few items to see structure
        def recurse_outline(items, depth=0):
            for item in items:
                if isinstance(item, list):
                    recurse_outline(item, depth + 1)
                else:
                    # pypdf outline items usually have 'title' and 'page' (which is a page object)
                    try:
                        title = item.title
                        # determining page number is tricky in pypdf, usually need helper
                        page_index = reader.get_page_number(item.page) + 1
                        print(f"{'  ' * depth}- Page {page_index}: {title[:50]}...")
                    except Exception as e:
                        print(f"{'  ' * depth}- [Error reading item: {e}]")
                if depth == 0 and items.index(item) > 4: # Only print first 5 root items
                     print("... (truncated)")
                     break
        
        recurse_outline(reader.outline)

    except Exception as e:
        print(f"Error: {e}")

inspect_outline(file_part_1)
inspect_outline(file_part_2)
