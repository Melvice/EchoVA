import speech_recognition as sr
from time import ctime
import time
import pywhatkit
import os
import random
from gtts import gTTS
import webbrowser
import pygame
import wikipedia
import pyjokes

pygame.mixer.init()
r = sr.Recognizer()

# create a function that execute commands input

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            echo_speak(ask)
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
            print("you said: "+ voice_data)
        except sr.UnknownValueError:
            echo_speak("Sorry, I did not get that")
        except sr.RequestError:
            echo_speak("Sorry, my speech service is down")
    return voice_data
    
def echo_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1,10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    print(audio_string)
    #delete audio_file once audio end
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.music.unload()
    os.remove(audio_file)
       
def command(voice_data):
    if 'what is your name' in voice_data:
        echo_speak("My name is Echo")
    if 'what time is it' in voice_data:
        echo_speak("The time is : " + ctime())
    if 'search' in voice_data:
        search = record_audio("What do you want to search for?")
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        echo_speak("Here is what I found for " + search)
    if 'song' in voice_data:
        song = record_audio("What song do you want to play?")
        pywhatkit.playonyt(song)
        echo_speak("Here is what I found for " + song)
    if 'find location' in voice_data:
        location = record_audio("What location do you want to find?")
        url = "https://google.nl/maps/place/" + location + "/&amp;"
        webbrowser.get().open(url)
        echo_speak("Here is the location of " + location)
    if 'who is' in voice_data:
        wiki = record_audio("Who is the person you want to know?")
        info = wikipedia.summary(wiki, 1)
        echo_speak("Here is what I found on wikipedia" + info)
    if 'joke' in voice_data:
        echo_speak(pyjokes.get_joke())
    if 'exit' in voice_data:
        echo_speak("It's been nice talking to you! goodbye")
        exit()
    
time.sleep(1)
echo_speak("Hello! How can i help you?")
while 1:
    voice_data = record_audio()
    command(voice_data)