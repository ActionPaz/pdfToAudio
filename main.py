from gtts import gTTS
from PyPDF2 import PdfReader

file_name = input("Enter the name of the pdf file: ")

text = ""
with open(file_name, "rb") as file:
    reader = PdfReader(file)
    for page in reader.pages:
        text += page.extract_text()

tts = gTTS(text)
tts.save("audiobook.mp3")


