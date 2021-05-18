# Importing Modules

from gtts import gTTS
import re
import pytesseract
import os
try:
    from PIL import Image
except ImportError:
    import Image

from speech_recognition import Microphone, Recognizer, AudioFile, RequestError, UnknownValueError

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# Text Detection from Image

path='Walmart.png'
info_text = pytesseract.image_to_string(Image.open(path))
print(info_text)

# storing the image data in file

f = open("recipt_text.txt", "w")
f.write(info_text)
f.close()

# Storing the text in List

receipt_text = info_text.split()
#print(receipt_text)

# Converting text to lowercase

for i in range(len(receipt_text)):
    receipt_text[i] = receipt_text[i].lower()

#print(receipt_text)

# speech as input from user

rec = Recognizer()
mic = Microphone()

with mic:
    print("Talk Now")
    audio = rec.record(mic, 5)

try:
    recognized = rec.recognize_google(audio)
    print("You said : ", recognized)

except RequestError as exc:
    print(exc)

except UnknownValueError:
    print("Unable to recognize")

# Tokens


def Convert(string):
	li = list(string.split(" "))
	return li

li = Convert(recognized)
print(li)

#######

articles = {'a','of','only','for','an'}

li = [ele for ele in li if ele not in articles]
print(li)

#######

import numpy as np
recognized_text = np.asarray(li)

for i in range(len(li)):
   recognized_text[i] = recognized_text[i].lower()


print(recognized_text)
print(type(recognized_text))

##########

# program to print date


# program to print date
for j in range(len(recognized_text)):
    if (recognized_text[j] == 'date'):
        import re

        f = open("recipt_text.txt", "r")
        content = f.read()
        pattern = "\d{2}[/-]\d{2}[/-]\d{4}"
        dates = re.findall(pattern, content)
        for date in dates:
            if "-" in date:
                day, month, year = map(int, date.split("-"))
            else:
                day, month, year = map(int, date.split("/"))
            if 1 <= day <= 31 and 1 <= month <= 12:
                print(date)
                text_val = date
        f.close()

# program to print time
for j in range(len(recognized_text)):
    if (recognized_text[j] == 'time'):
        regex = re.compile(r'\d{2}:\d{2}')
        with open('recipt_text.txt') as f:
            # text_val = regex.findall(f.read())
            # print(text_val)
            def listToString(s):
                str1 = ""
                for ele in s:
                    str1 += ele
                return str1


            text_val = listToString(text_val)
            print(text_val)

import re

count = 0
for i in range(0, len(receipt_text)):
    for j in range(0, len(recognized_text)):
        if (recognized_text[j] == receipt_text[i]):
            count += 1
            n = count

if (count == n):
    for i in range(0, len(receipt_text)):
        for j in range(0, len(recognized_text)):
            if (recognized_text[j] == receipt_text[i]):
                val = receipt_text[i]

for i in range(0, len(receipt_text)):
    for j in range(0, len(recognized_text)):
        if (receipt_text[i] == val):
            inval = i
            if (receipt_text[inval + 1].isalpha()):
                print(receipt_text[inval + 2])
                text_val = receipt_text[inval + 2]
                break
            else:
                print(receipt_text[inval + 1])
                text_val = receipt_text[inval + 1]
                break
# storing the output in a file


f = open("text.txt", "w")
f.write(text_val)
f.close()

# text to audio output

f=open('text.txt')
x=f.read()

language='en'

audio=gTTS(text=x,lang=language,slow=False)

audio.save("1.wav")
os.system("1.wav")