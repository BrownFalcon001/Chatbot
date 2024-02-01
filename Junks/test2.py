import streamlit as st
import PyPDF2
from io import BytesIO
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK resources (required for named entity recognition)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def extract_text_from_pdf(uploaded_file):
    text = ""
    with BytesIO(uploaded_file.read()) as f:
        reader = PyPDF2.PdfReader(f)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def semantic_similarity(question, passages):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(passages + [question])
    similarity_matrix = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    return similarity_matrix.flatten()

def named_entity_recognition(question, text):
    sentences = nltk.sent_tokenize(text)
    named_entities = []
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        pos_tags = nltk.pos_tag(words)
        chunked = nltk.ne_chunk(pos_tags)
        for subtree in chunked:
            if isinstance(subtree, nltk.Tree):
                entity = " ".join([word for word, tag in subtree.leaves()])
                named_entities.append(entity)
    return [entity for entity in named_entities if entity.lower() in question.lower()]

def text_summarization(text, max_sentences=5):
    sentences = nltk.sent_tokenize(text)
    summary = " ".join(sentences[:max_sentences])
    return summary

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
            # Semantic Similarity
            similarity_scores = semantic_similarity(user_question, nltk.sent_tokenize(pdf_text))
            top_passages_indices = similarity_scores.argsort()[-3:][::-1]  # Top 3 passages
            
            # Named Entity Recognition
            relevant_entities = named_entity_recognition(user_question, pdf_text)
            
            # Text Summarization
            pdf_summary = text_summarization(pdf_text)
            
            # Display results
            st.write("### Semantic Similarity Results:")
            for idx in top_passages_indices:
                st.write(nltk.sent_tokenize(pdf_text)[idx])
            
            st.write("### Named Entities mentioned in the question:")
            st.write(", ".join(relevant_entities))
            
            st.write("### Text Summary:")
            st.write(pdf_summary)

if __name__ == "__main__":
    main()
