import os
import sys
import tkinter as tk
from tkinter import filedialog

try:
    from pdf2image import convert_from_path
    import pytesseract
    from PIL import Image
except ImportError:
    print("Error: Missing dependencies. Please run:")
    print("pip install pytesseract pdf2image pillow")
    sys.exit(1)

# --- CONFIGURATION ---
# Tesseract Path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Poppler Path - Injecting into System PATH for internal utility access
POPPLER_PATH = r'C:\poppler-25.07.0\Library\bin'
os.environ["PATH"] += os.pathsep + POPPLER_PATH

def ocr_pdf_to_html(pdf_path):
    """
    Converts a single PDF to a reference HTML file using OCR.
    """
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_html = f"ref_{base_name}.html"
    
    print(f"\n>>> Processing: {pdf_path}")
    print(f"Opening PDF and converting to images...")
    
    try:
        # Convert PDF to images
        pages = convert_from_path(pdf_path, 300, poppler_path=POPPLER_PATH)
        
        html_content = [
            "<!DOCTYPE html>",
            "<html lang='hi'>",
            "<head><meta charset='UTF-8'><title>Reference: {base_name}</title></head>",
            "<body style='font-family: Arial; line-height: 1.6; padding: 40px; color: #334155;'>",
            f"<h1>Reference Content from: {os.path.basename(pdf_path)}</h1>",
            "<hr>"
        ]
        
        for i, page in enumerate(pages):
            print(f"OCR-ing Page {i+1} of {len(pages)}...")
            html_content.append(f"<h2>--- Page {i+1} ---</h2>")
            
            # Full page OCR using Hindi and English
            text = pytesseract.image_to_string(page, lang='hin+eng')
            html_content.append(f"<div class='ocr-full-page' style='white-space: pre-wrap; background: #f8fafc; padding: 20px; border: 1px solid #e2e8f0; margin-bottom: 20px;'>{text}</div>")

        html_content.append("</body></html>")
        
        with open(output_html, "w", encoding="utf-8") as f:
            f.write("\n".join(html_content))
        
        print(f"Done! Created: {output_html}")
        return True
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")
        return False

def select_files_and_process():
    # Hide the main tkinter window
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True) # Bring to front

    print("Opening file selection window...")
    file_paths = filedialog.askopenfilenames(
        title="Select PDF files for OCR",
        filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
    )

    if not file_paths:
        print("No files selected. Exiting.")
        return

    print(f"Selected {len(file_paths)} files.")
    
    success_count = 0
    for path in file_paths:
        if ocr_pdf_to_html(path):
            success_count += 1
            
    print(f"\n========================================")
    print(f"Batch Processing Complete!")
    print(f"Successfully processed: {success_count}/{len(file_paths)}")
    print(f"========================================")

if __name__ == "__main__":
    select_files_and_process()
