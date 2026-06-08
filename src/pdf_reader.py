from typing import List, Dict
import fitz

def extract_pdf_text(pdf_path:str):

    pages=[]
    try:
        pdf_doc=fitz.open(pdf_path)
        for page_num in range(len(pdf_doc)):
            page=pdf_doc.load_page(page_num)
            text=page.get_text("text").strip()
            pages.append(
                {
                    "page": page_num + 1,
                    "text": text
                }
            )
        pdf_doc.close()
        return pages

    except Exception as e:
        raise RuntimeError(
            f"Failed to read PDF: {e}"
        ) from e