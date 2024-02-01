import streamlit as st
import time  # Import time module
from PyPDF2 import PdfReader
from io import BytesIO
import nltk
from nltk.corpus import stopwords
from fuzzywuzzy import fuzz  # Import fuzzywuzzy for fuzzy string matching

# Download NLTK resources (required for text preprocessing)
nltk.download('punkt')
nltk.download('stopwords')

# Initialize session memory dictionary
session_memory = {}

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

def main():
    st.title("Chatbot for PDF Document Analysis")
    
    # Get or create session ID
    session_id = st.session_state.get("session_id", str(time.time()))
    st.session_state.session_id = session_id
    
    # Print session ID
    st.write(f"Session ID: {session_id}")
    
    # Check if session memory exists for the current session ID
    if session_id not in session_memory:
        session_memory[session_id] = {"cv_text": ""}
    
    # Upload CV file
    uploaded_file = st.file_uploader("Upload your CV", type="pdf")
    
    if uploaded_file:
        # Extract text from CV and store it in session memory
        cv_text = extract_text_from_pdf(uploaded_file)
        session_memory[session_id]["cv_text"] = cv_text
        
        # Start timer
        start_time = time.time()
        
        # User input keywords
        user_keywords = st.text_input("Enter keywords to search for in your CV (comma-separated):")
        
        if user_keywords:
            # Split user input keywords into a list
            keywords = [keyword.strip() for keyword in user_keywords.split(",")]
            
            # Extract information based on keywords
            extracted_info = extract_information(session_memory[session_id]["cv_text"], keywords)
            
            # Display extracted information
            if extracted_info:
                response = {"response": extracted_info}
                st.json(response)  # Display response in JSON format
            else:
                response = {"response": "No information found in your CV based on the provided keywords."}
                st.json(response)  # Display response in JSON format
        
        # Calculate response time
        response_time = time.time() - start_time
        st.write(f"Response time: {response_time:.2f} seconds")

if __name__ == "__main__":
    main()
