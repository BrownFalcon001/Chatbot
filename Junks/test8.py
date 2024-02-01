import streamlit as st
import time
from PyPDF2 import PdfReader
from io import BytesIO
import nltk
from nltk.corpus import stopwords
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree

# Download NLTK resources (required for text preprocessing)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('maxent_ne_chunker')
nltk.download('words')

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
    # Perform named entity recognition (NER)
    for sent in nltk.sent_tokenize(pdf_text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if isinstance(chunk, Tree):
                # Check if the chunk represents a named entity
                entity = " ".join([token for token, pos in chunk.leaves()])
                # Add the full line containing the named entity
                line = sent.split(entity)[0] + entity + sent.split(entity)[-1]
                extracted_info.append(line.strip())
    return extracted_info

def main():
    st.title("CV Chatbot")
    
    # Upload CV file
    uploaded_file = st.file_uploader("Upload your CV", type="pdf")
    
    if uploaded_file:
        # Start timer
        start_time = time.time()
        
        # Extract text from CV
        cv_text = extract_text_from_pdf(uploaded_file)
        
        # User input keywords
        user_keywords = st.text_input("Enter keywords to search for in your CV (comma-separated):")
        
        if user_keywords:
            # Split user input keywords into a list
            keywords = [keyword.strip() for keyword in user_keywords.split(",")]
            
            # Extract information based on NER
            extracted_info = extract_information(cv_text, keywords)
            
            # Display extracted information
            if extracted_info:
                response = {"response": extracted_info}
                st.json(response)  # Display response in JSON format
            else:
                response = {"response": "No relevant information found in your CV based on the provided keywords."}
                st.json(response)  # Display response in JSON format
        
        # Calculate response time
        response_time = time.time() - start_time
        st.write(f"Response time: {response_time:.2f} seconds")

if __name__ == "__main__":
    main()
