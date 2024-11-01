# resume_parser.py

from pdfminer.high_level import extract_text
from affinda import AffindaAPI, TokenCredential
import os

def parse_pdf(file_path):
    #connect to api
    api_key = "aff_410d75bacbe972f7e6e565c236e9baae2768d1e9"
    credential = TokenCredential(api_key)
    client = AffindaAPI(credential)
    with open(file_path, "rb") as file:
        document = client.create_document(
            file=file,
            file_name="document.pdf",
            collection="iSqVazxq"
        )
    parsed_data = document.as_dict()
    #at this point, parsed_data has all the text
    skills = parsed_data.get("data", {}).get("skills",[])
    experiences = parsed_data.get("data", {}).get("work_experience", [])
    # Compile keywords based on skills and experience job titles
    keywords = [skill["name"] for skill in skills]  # Extracts only skill names
    job_titles = [exp["job_title"] for exp in experiences if "job_title" in exp]
    return(keywords + job_titles)  # Combine skills and job titles as keywords
