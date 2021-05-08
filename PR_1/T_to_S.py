from gtts import gTTS
import os

fh = open("test.txt","r")

mytext = fh.read().replace("\n"," ")

language = 'en'

out = gTTS(text=mytext, lang=language, slow=False)

out.save('speech.mp3')

os.system('start speech.mp3')

# Text to speech conversion from a file