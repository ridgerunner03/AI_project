# -*- coding: utf-8 -*-
"""
This is the very first A.I. in this series.  
The vision is to devlop 'protocol droid' to talk to, to help with tasks, and with whom to play games.
The droid will be able to translate langages and connect ppl.


"""

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import dadjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("hey, My name is 'lisa, human cyborg relations. Please see the console for what I can do for you.")
#engine.say("hey, .")
engine.runAndWait()
print("I can play videos (Lisa, play....),\n teach (Lisa, teach me about...),\n tell you more (Lisa, tell me more about...),\n tell time (Lisa, what time is it),\n and tell jokes (Lisa, tell me a joke...).")

def talk(text):
    engine.say("heyo"+text)
    engine.runAndWait()



def take_command():

    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'lisa' in command:
               command = command.replace('lisa','')
               
            
                
                
        
    except:
        print("something went wrong")
    
    
    return command
def run_lisa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play','')
        talk('hey playing' + song)
        print('playing...'+ song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        #needs a more natural way of expressing time
        #i would like mil time
        time = datetime.datetime.now().strftime('%H %M')
        talk('Right now it is '+time)
    elif "teach me about" in command:
        info = command.replace('teach me about','')
        teach = wikipedia.summary(info,2)
        print(teach)
        talk(teach)
    elif "tell me more about" in command:
        info = command.replace('tell me more about','')
        teach = wikipedia.summary(info,6)
        print(teach)
        talk(teach)
    elif "joke" in command:
        talk(dadjokes.joke())
    elif "good one" in command:
        talk("yeah thanks!  I'll be here all week folks!")
    
    
    
    
    
    
    
    
    
while True:        
    run_lisa()
        