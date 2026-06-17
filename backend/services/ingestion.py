import fitz #This is what PyMuPDF is called when we import it

def parse_pdf(file_path: str) -> str:
    """Open a PDF file and pull out all of it's text as one big string."""
    doc = fitz.open(file_path)

    all_text = ""
    for page in doc:
        all_text += page.get_text()

    doc.close()
    return all_text
