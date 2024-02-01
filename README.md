# Chatbot for PDF Document Analysis

Chatbot for PDF Document Analysis is a Python application that allows users to upload a PDF document and extract specific information from it based on keywords provided by the user. The chatbot utilizes natural language processing (NLP) techniques to analyze the content of the document and extract relevant information.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture Diagram](#architecture-diagram)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
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

To run the Chatbot for PDF Document Analysis locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/pdf-chatbot.git
