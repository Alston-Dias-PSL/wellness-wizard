import fitz  # PyMuPDF
from typing import List
from pydantic import BaseModel

class PdfProcessor:

    def read_pdf(self, file_path: str) -> str:
        with fitz.open(file_path) as pdf_document:
            text = ''
            for page_num in range(pdf_document.page_count):
                text += pdf_document[page_num].get_text()
            return text