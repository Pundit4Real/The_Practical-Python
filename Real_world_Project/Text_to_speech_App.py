# IN this program, we are writing a python program that translate text to speech using the pttsx3.

import pyttsx3 
import os
myFile = open("hello.txt", "r" )
myText = myFile.read()

voice = pyttsx3.init()
voice.say(myText)
voice.save_to_file(myText, "python.mp3")
voice.runAndWait()
os.system("start python.mp3")


