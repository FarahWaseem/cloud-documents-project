import fitz  # PyMuPDF
from docx import Document

def extract_pdf_title(pdf_path):
    doc = fitz.open(pdf_path)
    first_page = doc.load_page(0)
    text = first_page.get_text("text")
    lines = text.split('\n')
    for line in lines:
        if line.strip():
            return line.strip()
    return "No Title Found"

def extract_docx_title(docx_path):
    doc = Document(docx_path)
    for para in doc.paragraphs:
        text = para.text.strip()
        if text:
            return text
    return "No Title Found"

pdf_file = "sample.pdf"
docx_file = "sample.docx"

print("PDF Title:", extract_pdf_title(pdf_file))
print("Word Title:", extract_docx_title(docx_file))
