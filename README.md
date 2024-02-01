# Chatbot for PDF Document Analysis

## Overview
This project implements a chatbot that analyzes text from uploaded PDF documents and provides responses based on user queries. The chatbot extracts information from the PDF documents using natural language processing techniques and responds to user queries in real-time.

## Approach
The chatbot is built using Python and Streamlit for the user interface. It utilizes the PyPDF2 library for PDF processing, NLTK for text preprocessing, and fuzzywuzzy for fuzzy string matching. The architecture follows a simple client-server model, where the Streamlit app serves as the front end and communicates with the backend API.

### Architecture Diagram
![Architecture Diagram](architecture_diagram.png)

## Screenshots
### Home Page
![Home Page](screenshots/home_page.png)

### Uploaded PDF and User Input
![Uploaded PDF and User Input](screenshots/uploaded_pdf.png)

### Response Display
![Response Display](screenshots/response_display.png)

## Dependencies
- Python 3.x
- Streamlit
- PyPDF2
- NLTK
- Fuzzywuzzy

## Setup Instructions
1. Clone this repository to your local machine.
2. Install the required dependencies using the following command:
