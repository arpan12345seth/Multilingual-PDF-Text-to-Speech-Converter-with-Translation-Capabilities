# Multilingual-PDF-Text-to-Speech-Converter-with-Translation-Capabilities

## Overview
This project presents an innovative system designed to extract text from PDF documents and convert it into speech in multiple languages. It integrates text extraction, translation, and text-to-speech technologies to create accessible audio formats of documents, primarily benefiting users with visual disabilities or language barriers. 

Users can upload a PDF, select a preferred language, and listen to the original or translated text in audio format. Built on a web framework, this platform emphasizes inclusivity and accessibility.

---

## Features
- **Multilingual Translation**: Utilizes Google Translate API to support numerous languages.
- **PDF Text Extraction**: Extracts text from various types of PDFs using PyMuPDF.
- **Text-to-Speech Conversion**: Converts text into speech using Google Text-to-Speech (gTTS).
- **User-Friendly Interface**: A web-based platform powered by Flask, enabling easy navigation.
- **Cross-Platform Compatibility**: Ensures seamless functionality across devices and screen sizes.


## Installation
### Prerequisites
- Python 3.8+
- Flask
- PyMuPDF
- Google Translate API
- gTTS

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/arpan12345seth/Multilingual PDF Text-to-Speech Converter with Translation Capabilities.git
    cd Multilingual PDF Text-to-Speech Converter with Translation Capabilities
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the application:
    ```bash
    python app.py
    ```
4. Access the platform in your browser at `http://127.0.0.1:5000`.
