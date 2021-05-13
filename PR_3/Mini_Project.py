import cv2
import numpy as np
import pytesseract
import easyocr
from PIL import Image
from speech_recognition import Microphone, Recognizer, AudioFile, RequestError, UnknownValueError


#Reading Text from image - Step_1
read = easyocr.Reader(['en'])
out = read.readtext('Recipt1.jpg')

#Slicing the words - Step_2

o = []
for i in range(len(out)):
  o.append(out[i][1])


#Converting list to array - Step_3


import numpy as np
my_array = np.asarray(o)

for i in range(len(my_array)):
   my_array[i] = my_array[i].lower()


#Removing spaces - Step_4

my_array1 = []
for i in my_array:
    j = i.replace(' ','')
    my_array1.append(j)
print(my_array1)


#Giving Speech As Input - Step_5

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

#Converting Speech into tokens - Step_6

arr = recognized.split()
print(arr)

#Finding the matched words - Step_7

for i in range(0,len(my_array)):
  for j in range(0,len(arr)):
    if(arr[j] == my_array[i]):
      print("match")
      val = arr[j]
      count = 0
      for i in my_array:
        count+=1
        if(i == val):
          print("The overall cost of " + val + " is:  " + my_array[count])
          text_val = my_array[count]
          break

f = open("output.txt", "w")
f.write(text_val)
f.close()

from gtts import gTTS

import os

f=open('output.txt')
x= f.read()
language='en'

audio=gTTS(text=x,lang=language,slow=False)

audio.save("1.wav")
os.system("1.wav")

