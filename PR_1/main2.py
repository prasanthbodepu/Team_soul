import pytesseract
from PIL import Image
import os

# C:\Program Files\Tesseract-OCR

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

img = Image.open('samp1.jpeg')
text = pytesseract.image_to_string(img)
print(text)

# Image to Text Conversion
