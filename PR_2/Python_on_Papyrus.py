from speech_recognition import Microphone, Recognizer, AudioFile

rec = Recognizer()
mic = Microphone()

with mic:
    print("Talk Now")
    audio = rec.record(mic, 5)

recognized = rec.recognize_google(audio)
print("You said : ", recognized)