from flask import Flask, request, render_template
from resume_parser import parse_pdf
from job_searcher import search_jobs

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
    return f"<h2>parsed: {file_text} </h2>"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)  # Listen on all interfaces, not just localhost


