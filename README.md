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

## Architecture Diagram

![Architecture Diagram](architecture_diagram.png)

## Setup Instructions

To run the Chatbot for PDF Document Analysis locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/pdf-chatbot.git
