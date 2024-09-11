import fitz
from docx import Document


def read_text(file):
    text = file.read().decode('utf-8','ignore')
    return text

def read_pdf(file):
    try:
        # Open the PDF file
        pdf_document = fitz.open(stream=file.read(), filetype="pdf")
        pdf_text = ""

        # Extract text from each page
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            pdf_text += page.get_text()
        return pdf_text
    
    except Exception as e:
        return f"Error reading pdf {e}"

def read_doc(file):
    try:
        document = Document(file)
        docx_text = "\n".join([para.text for para in document.paragraphs])
        return docx_text
    except Exception as e:
        return (f"Error reading DOCX file: {e}")