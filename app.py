from flask import Flask, request, jsonify
import time
from PyPDF2 import PdfReader
from io import BytesIO
import nltk
from nltk.corpus import stopwords
from fuzzywuzzy import fuzz

# Initialize Flask app
app = Flask(__name__)

# Download NLTK resources (required for text preprocessing)
nltk.download('punkt')
nltk.download('stopwords')

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    text = ""
    with BytesIO(uploaded_file.read()) as f:
        reader = PdfReader(f)
        for page in reader.pages:
            text += page.extract_text()
    return text

# Function to preprocess text
def preprocess_text(text):
    # Tokenize text
    tokens = nltk.word_tokenize(text)
    # Remove punctuation and stopwords
    stop_words = set(stopwords.words('english'))
    words = [word.lower() for word in tokens if word.isalnum() and word.lower() not in stop_words]
    return " ".join(words)

# Function to extract specific information from PDF text based on keywords
def extract_information(pdf_text, keywords):
    extracted_info = []
    for keyword in keywords:
        keyword = keyword.lower()
        for line in pdf_text.split('\n'):
            # Use fuzzy string matching to find approximate matches
            if fuzz.partial_ratio(keyword, line.lower()) >= 80:  # Adjust threshold as needed
                extracted_info.append(line.strip())
    return extracted_info

@app.route('/get_response/<session_id>/<pdf_name>/<query_question>', methods=['GET'])
def get_response(session_id, pdf_name, query_question):
    # Process PDF file
    uploaded_file = request.files['pdf_file']
    cv_text = extract_text_from_pdf(uploaded_file)
    
    # Preprocess text
    cv_text = preprocess_text(cv_text)
    
    # Extract information based on query question
    extracted_info = extract_information(cv_text, [query_question])
    
    # Construct response
    response = {"response": extracted_info}
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
