from typing import List, Optional
import os
from pypdf import PdfReader, PdfWriter


class PDFExtractor:
    """
    A class to handle PDF page extraction operations efficiently.

    Attributes:
        source_path (str): The file path to the source PDF document.
    """

    def __init__(self, source_path: str):
        """
        Initializes the PDFExtractor with the source file path.

        Args:
            source_path (str): Path to the source PDF file.

        Raises:
            FileNotFoundError: If the source file does not exist.
        """
        if not os.path.exists(source_path):
            raise FileNotFoundError(f"The file '{source_path}' was not found.")
        self.source_path = source_path
        self._reader = None  # Cache the reader

    @property
    def reader(self):
        if self._reader is None:
            self._reader = PdfReader(self.source_path)
        return self._reader

    def extract_section(self, start_page: int, end_page: int, output_filename: str) -> None:
        """
        Extracts a specific range of pages from the source PDF and saves it as a new file.
        
        Args:
            start_page (int): The starting page number (1-based index).
            end_page (int): The ending page number (1-based index, inclusive).
            output_filename (str): The name of the output PDF file.
        """
        # Validate input logic
        if start_page < 1 or end_page < start_page:
            raise ValueError(f"Invalid page range: {start_page} to {end_page}")

        writer = PdfWriter()
        total_pages = len(self.reader.pages)

        if end_page > total_pages:
            print(f"Warning: end_page ({end_page}) exceeds total pages ({total_pages}). Clipping to max.")
            end_page = total_pages

        # Loop through the range and add pages to writer
        for i in range(start_page - 1, end_page):
            writer.add_page(self.reader.pages[i])

        # Ensure directory exists
        output_dir = os.path.dirname(output_filename)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)

        with open(output_filename, "wb") as output_file:
            writer.write(output_file)

        print(f"[SUCCESS] Extracted pages {start_page}-{end_page} to '{output_filename}'")

    def find_and_extract_by_title(self, title_query: str, output_filename: str) -> bool:
        """
        Searches for a paper by title in the PDF outline/bookmarks and extracts it.
        The end page is inferred from the start of the next bookmark.
        
        Args:
            title_query (str): A distinct part of the title to search for (case-insensitive).
            output_filename (str): Where to save the extracted PDF.
            
        Returns:
            bool: True if found and extracted, False otherwise.
        """
        outline = self.reader.outline
        if not outline:
            print(f"[WARNING] No outline found in {os.path.basename(self.source_path)}. Cannot search by title.")
            return False

        found_start_page = -1
        found_end_page = -1
        
        # Flatten outline into a list of (title, page_number, level) tuples
        flat_outline = []

        def recurse_outline(items, level=0):
            for item in items:
                if isinstance(item, list):
                    recurse_outline(item, level + 1)
                else:
                    try:
                        # pypdf >= 3.0.0
                        page_index = self.reader.get_page_number(item.page) + 1
                        flat_outline.append((item.title, page_index, level))
                    except Exception:
                        continue
        
        recurse_outline(outline)
        
        # Search for the title
        matched_idx = -1
        matched_level = -1
        for i, (title, page_num, level) in enumerate(flat_outline):
            if title_query.lower() in title.lower():
                matched_idx = i
                found_start_page = page_num
                matched_level = level
                print(f"[FOUND] Match: '{title}' (Page {page_num}, Level {level})")
                break
        
        if matched_idx == -1:
            print(f"[NOT FOUND] Could not find title containing: '{title_query}'")
            return False

        # Determine end page: Stop at next item with level <= matched_level
        # Logic: If we are at Level 1 (Paper), skip all Level 2+ (Sections). Stop at next Level 1 or Level 0.
        found_end_page = len(self.reader.pages)
        
        for k in range(matched_idx + 1, len(flat_outline)):
            next_title, next_start_page, next_level = flat_outline[k]
            
            # If we hit a node that is a sibling (same level) or parent (lower level number), it's the boundary.
            if next_level <= matched_level:
                found_end_page = next_start_page - 1
                break
            
        # Safety check: if end page < start page, set to start page (1 page paper)
        if found_end_page < found_start_page:
            found_end_page = found_start_page

        print(f"[INFO] Extracting range: {found_start_page} to {found_end_page}")
        self.extract_section(found_start_page, found_end_page, output_filename)
        return True


# --- USAGE EXAMPLE (WORKFLOW) ---

# Define your source files (assuming you uploaded them to Colab/Local)
# Note: Ensure the filenames match exactly what you have on disk
