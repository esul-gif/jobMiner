from flask import Flask, request, render_template
from resume_parser import parse_pdf, extract_keywords

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
        # Save the file and parse it
        file.save(file.filename)
        text = parse_pdf(file.filename)
        keywords = extract_keywords(text)
        return f"Extracted Keywords: {keywords}"

if __name__ == '__main__':
    app.run(debug=True)

