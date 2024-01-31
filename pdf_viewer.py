import streamlit as st
import PyPDF2

def read_pdf(uploaded_file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    num_pages = len(pdf_reader.pages)
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text


def main():
    st.title("PDF Viewer")

    # File upload section
    st.sidebar.title("Upload PDF")
    uploaded_file = st.sidebar.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        st.sidebar.success("File successfully uploaded!")
        st.markdown("---")
        st.header("PDF Content")

        # Read and display PDF content
        pdf_content = read_pdf(uploaded_file)
        st.text(pdf_content)



if __name__ == "__main__":
    main()
