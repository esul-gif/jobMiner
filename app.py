from flask import Flask, request, render_template
from resume_parser import parse_pdf
from job_searcher import search_jobs

import sqlite3

def init_db():
    conn = sqlite3.connect("keywords.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Keywords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            keywords TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_keywords_to_db(keywords):
    # Join the list into a single string with commas separating each keyword
    keywords_str = ", ".join(keywords)  # Convert list to string
    conn = sqlite3.connect("keywords.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Keywords (keywords) VALUES (?)", (keywords_str,))
    conn.commit()
    conn.close()



init_db()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        # Save the uploaded file
        file_path = f"uploads/{file.filename}"
        file.save(file_path)
    
    file_text = parse_pdf(file_path)
        #return notice that file uploaded
    save_keywords_to_db(file_text)
    return f"<h2>parsed: {file_text} </h2>"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)  # Listen on all interfaces, not just localhost


