# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import speech_recognition
import pyttsx3

recognizer = speech_recognition.Recognizer()

print('Powiedz coś wyraźnie i głośno: ')
while True:

    try:

        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

           # text = recognizer.recognize_google(audio)
            text = recognizer.recognize_google(audio, language="pl-PL")
            text = text.lower()

            print(text)

    except speech_recognition.UnknownValueError:

        recognizer = speech_recognition.Recognizer()
        continue
pass
