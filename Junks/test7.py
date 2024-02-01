import streamlit as st
import time
from PyPDF2 import PdfReader
from io import BytesIO
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import fuzz

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

# Function to extract specific section from CV text based on keywords or patterns
def extract_section(cv_text, section_name):
    sentences = sent_tokenize(cv_text)
    section_start = -1
    section_end = -1
    section_name = section_name.lower()
    for i, sentence in enumerate(sentences):
        if fuzz.partial_ratio(section_name, sentence.lower()) >= 80:
            section_start = i
            break
    if section_start != -1:
        for i in range(section_start+1, len(sentences)):
            if sentences[i] == '':
                section_end = i
                break
    if section_start != -1 and section_end != -1:
        return ' '.join(sentences[section_start+1:section_end])
    return None

def main():
    st.title("CV Chatbot")
    
    # Upload CV file
    uploaded_file = st.file_uploader("Upload your CV", type="pdf")
    
    if uploaded_file:
        # Start timer
        start_time = time.time()
        
        # Extract text from CV
        cv_text = extract_text_from_pdf(uploaded_file)
        
        # User input section name
        user_section = st.text_input("Enter the section name you want to extract from your CV (e.g., 'skills'):")
        
        if user_section:
            # Extract section based on user input
            extracted_section = extract_section(cv_text, user_section)
            
            # Display extracted section
            if extracted_section:
                st.write("### Extracted Section:")
                st.write(extracted_section)
            else:
                st.write(f"No '{user_section}' section found in your CV.")
        
        # Calculate response time
        response_time = time.time() - start_time
        st.write(f"Response time: {response_time:.2f} seconds")

if __name__ == "__main__":
    main()
