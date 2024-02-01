import streamlit as st
import PyPDF2
from io import BytesIO

def extract_text_from_pdf(uploaded_file):
    text = ""
    with BytesIO(uploaded_file.read()) as f:
        reader = PyPDF2.PdfReader(f)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def main():
    st.title("PDF Chatbot")
    
    # Upload PDF file
    uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
    
    if uploaded_file:
        # Extract text from PDF
        pdf_text = extract_text_from_pdf(uploaded_file)
        
        # User input question
        user_question = st.text_input("Ask a question about the PDF:")
        
        if user_question:
            # Simple keyword matching for answer
            if user_question.lower() in pdf_text.lower():
                st.success("Yes, the document contains information related to your question.")
            else:
                st.error("Sorry, I couldn't find relevant information in the document.")

if __name__ == "__main__":
    main()
