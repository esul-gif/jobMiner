# resume_parser.py

from pdfminer.high_level import extract_text

def parse_pdf(file_path):
    #Extracts text from a PDF file.
    text = extract_text(file_path)
    return text

print(parse_pdf("uploads/ES.Resume.pdf"))