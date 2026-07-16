from app.parser.pdf_parser import PDFParser


def test_parser_initializes_with_pdf_path():
    parser = PDFParser("data/ct200_manual.pdf")
    assert parser.pdf_path == "data/ct200_manual.pdf"
