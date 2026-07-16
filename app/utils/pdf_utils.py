from pathlib import Path

import fitz


def extract_text_from_pdf(pdf_path: str) -> str:
    path = Path(pdf_path)
    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    doc = fitz.open(str(path))
    text_chunks = []
    for page in doc:
        text_chunks.append(page.get_text())
    return "\n".join(text_chunks)
