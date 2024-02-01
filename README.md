# Chatbot for PDF Document Analysis

Chatbot for PDF Document Analysis is a Python application that allows users to upload a PDF document and extract specific information from it based on keywords provided by the user. The chatbot utilizes natural language processing (NLP) techniques to analyze the content of the document and extract relevant information.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Setup Instructions](#setup-instructions)
- [Dependencies](#dependencies)
- [Future Scope](#future-scope)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Chatbot for PDF Document Analysis is built using Python and Streamlit, a popular library for building web applications with Python. It allows users to upload a PDF document, enter keywords of interest, and then extracts and displays information from the document relevant to those keywords.

## Features

- Upload PDF document
- Enter keywords to search for in the document
- Extract specific information from the document based on keywords using FuzzyWuzzy for fuzzy string matching
- Display extracted information in JSON format
- Calculate and display response time

## Architecture

The Chatbot for PDF Document Analysis follows a simple yet effective architecture, consisting of the following components:

1. **User Interface (Streamlit):** Provides a user-friendly interface for users to interact with the chatbot.
   
2. **Text Preprocessing Module (NLTK):** Handles text preprocessing tasks such as tokenization, removing stopwords, and normalizing text.

3. **PDF Text Extraction:** Utilizes the PyPDF2 library to extract text content from uploaded PDF documents.

4. **Keyword Extraction:** Employs the FuzzyWuzzy library for fuzzy string matching to extract specific information from the PDF text based on user-provided keywords.

5. **Response Generation:** Generates responses in JSON format containing the extracted information from the document.

6. **Performance Measurement:** Calculates and displays the response time for each query to provide users with an idea of processing speed.

This architecture ensures a streamlined workflow for document analysis, from user input to information extraction and response generation.


## Setup Instructions

To run the Chatbot for PDF Document Analysis locally on your machine, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/BrownFalcon001/Chatbot.git
```

### 2. Navigate to the Project Directory

```bash
cd Chatbot
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
### 4. Run the Application

```bash
streamlit run chatbot.py
```
### 5. Upload PDF Documents

Once the application is running, access it through the provided URL (usually http://localhost:8501) in your web browser. You can then upload PDF documents to analyze.

### 6. Enter Keywords

Enter keywords in the provided text input field to search for specific information within the uploaded PDF document.

### 7. View Results

The chatbot will display the extracted information based on the provided keywords in JSON format, along with the response time for each query.


## Note:

1. **Python Installation:** Ensure that you have Python installed on your system to run the application.

2. **Internet Connection:** Make sure you have an active internet connection during the first run of the application to download NLTK resources.

3. **Additional Dependencies:** The application may require additional dependencies based on your system configuration. Please refer to the requirements.txt file for details.

4. **Junk Folder:** It contains some tests I made during developing the chatbot


### Future Scope

1. **Implement more advanced natural language processing techniques for better understanding and response generation.**
2. **Add support for other document formats such as DOCX, TXT, etc.**
3. **Enhance the user interface with more interactive features.**
4. **Integrate authentication and authorization for secure access.**
5. **Implement a database backend for storing and retrieving session data.**




