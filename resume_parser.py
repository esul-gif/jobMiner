# resume_parser.py

from pdfminer.high_level import extract_text
import spacy
import pytextrank

# Load spaCy model, a NLP model that works with PyTextRank to rank keywords
nlp = spacy.load("en_core_web_sm")
    # Add PyTextRank to the spaCy pipeline
nlp.add_pipe("textrank")

common_keywords = {
    "Python", "JavaScript", "SQL", "Excel", "Machine Learning", "Project Management",
    "Communication", "Leadership", "Data Analysis", "Microsoft Office", "Java", "C++",
    "React", "AWS", "Django", "Tableau", "Business Intelligence", "Marketing", "Sales",
    "Engineering", "Education", "Experience", "Skills", "Training", "Internship"
}

def parse_pdf(file_path):
    text = extract_text(file_path)
    # Process the text with spaCy
    doc = nlp(text)
    # Extract top-ranked keywords
    key_words = []
    for phrase in doc._.phrases[:10]:  # Limiting to top 5 keywords for simplicity
        key_words.append(phrase.text)
        #return(phrase.text)
    return key_words

print(parse_pdf("uploads/ES.Resume.pdf"))