from flask import Flask, render_template, request, url_for
import fitz  # PyMuPDF
from googletrans import Translator
from gtts import gTTS
import gtts.lang
import os

app = Flask(__name__)

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def translate_text(text, dest_language):
    translator = Translator()
    translated = translator.translate(text, dest=dest_language)
    return translated.text

def text_to_speech(text, lang_code, output_file):
    tts = gTTS(text=text, lang=lang_code)
    tts.save(output_file)
    return output_file

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Save the uploaded PDF file
        pdf_file = request.files["pdf"]
        pdf_path = os.path.join("uploads", pdf_file.filename)
        pdf_file.save(pdf_path)

        # Get the destination language from user input
        dest_language = request.form["language"]

        # Extract text from the PDF
        extracted_text = extract_text_from_pdf(pdf_path)

        # Translate the extracted text to the selected language
        translated_text = translate_text(extracted_text, dest_language)

        # Convert the original text to speech (default in English)
        original_voice_file = text_to_speech(extracted_text, lang_code='en', output_file="static/original_output.mp3")

        # Convert the translated text to speech
        translated_voice_file = text_to_speech(translated_text, lang_code=dest_language, output_file="static/translated_output.mp3")

        # Return the original text, translated text, and audio file URLs
        return render_template("result.html",
                               original_text=extracted_text,
                               translated_text=translated_text,
                               original_voice_url=url_for('static', filename='original_output.mp3'),
                               translated_voice_url=url_for('static', filename='translated_output.mp3'))

    # Get the list of supported languages for text-to-speech
    supported_languages = gtts.lang.tts_langs()
    return render_template("index.html", languages=supported_languages)

if __name__ == "__main__":
    os.makedirs("uploads", exist_ok=True)
    os.makedirs("static", exist_ok=True)
    app.run(debug=True)
