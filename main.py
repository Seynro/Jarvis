import pyttsx3
from decouple import config

from datetime import datetime

import speech_recognition as sr
from random import choice
from utils import opening_text

USERNAME = 'Seymur'
BOTNAME = 'Jarvis'



engine = pyttsx3.init()

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def greet_user():
    """Greets the user according to the time"""

    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        engine.say(f"Good Morning {USERNAME}")
        engine.runAndWait()
    elif (hour >= 12) and (hour < 16):
        engine.say(f"Good afternoon {USERNAME}")
        engine.runAndWait()
    elif (hour >= 16) and (hour < 19):
        engine.say(f"Good Evening {USERNAME}")
        engine.runAndWait()
    engine.say(f"I am {BOTNAME}. How may I assist you?")
    engine.runAndWait()


def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='ru-RU')
        if not 'exit' in query or 'stop' in query:
            engine.say(choice(opening_text))
            engine.runAndWait()
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                engine.say("Good night sir, take care!")
                engine.runAndWait()
            else:
                engine.say('Have a good day sir!')
                engine.runAndWait()
            exit()
    except Exception:
        engine.say('Sorry, I could not understand. Could you please say that again?')
        engine.runAndWait()
        query = 'None'
    return query

#--------------------------------------------------------------------------------
#SPOTIFY
#KEYBORD
import keyboard

import json
import spotipy
import webbrowser

username = 'woo9l14m24zfhoxu8ogr546zd'
clientID = 'e97d5d276e8245018f89735856161ce2'
clientSecret = '5716b63696d3495787e0cb3d8e18bbb3'
redirect_uri = 'http://google.com/callback/'
def open_spotify(username, clientSecret, clientID,redirect_uri):

    oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
    token_dict = oauth_object.get_access_token()
    token = token_dict['access_token']
    spotifyObject = spotipy.Spotify(auth=token)
    user_name = spotifyObject.current_user()

    # To print the response in readable format.
    print(json.dumps(user_name, sort_keys=True, indent=4))


    while True:
        print("Welcome to the project, " + user_name['display_name'])
        print("no - Exit the console")
        print("yes - Search for a Song")
        print("Enter Your Choice: ")
        engine.say("Welcome to the project, " + user_name['display_name'])
        engine.runAndWait()
        engine.say("0 - Exit the console")
        engine.runAndWait()
        engine.say("1 - Search for a Song")
        engine.runAndWait()
        engine.say("Enter Your Choice: ")
        engine.runAndWait()
        user_input = take_user_input().lower()
        if user_input == 'yes':
            print("Enter the song name: ")
            search_song = take_user_input().lower()
            results = spotifyObject.search(search_song, 1, 0, "track")
            songs_dict = results['tracks']
            song_items = songs_dict['items']
            song = song_items[0]['external_urls']['spotify']
            webbrowser.open(song)
            print('Song has opened in your browser.')
            engine.say('Song has opened in your browser.')
            engine.runAndWait()
        else:
            print("Good Bye, Have a great day!")
            engine.say("Good Bye, Have a great day!")
            engine.runAndWait()
            break


#--------------------------------------------------------------------------------


import requests
from online_ops import get_random_joke, play_on_youtube, search_on_google, send_whatsapp_message
from os_ops import open_google, open_photoshop, open_calculator
from pprint import pprint


if __name__ == '__main__':
    greet_user()

    while True:
        query = take_user_input().lower()
        if 'open photoshop' in query:
            open_photoshop()

        if 'open google' in query:
            open_google()

        if 'open calculator' in query:
            open_calculator()

        if 'youtube' in query:
            engine.say('What do you want to play on Youtube, sir?')
            engine.runAndWait()
            video = take_user_input().lower()
            play_on_youtube(video)

        if 'search on google' in query:
            engine.say('What do you want to search on Google, sir?')
            engine.runAndWait()
            query = take_user_input().lower()
            search_on_google(query)

        if "send whatsapp message" in query:
            engine.say('On what number should I send the message sir? Please enter in the console: ')
            engine.runAndWait()
            number = input("Enter the number: ")
            engine.say("What is the message sir?")
            engine.runAndWait()
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            engine.say("I've sent the message sir.")
            engine.runAndWait()

        if 'joke' in query:
            engine.say(f"Hope you like this one sir")
            engine.runAndWait()
            joke = get_random_joke()
            engine.say(joke)
            engine.runAndWait()
            engine.say("For your convenience, I am printing it on the screen sir.")
            engine.runAndWait()
            pprint(joke)

        if 'да' in query:
            engine.say('pizda, sir')
            engine.runAndWait()

        if 'нет' in query:
            engine.say('Pidora otvet, sir')
            engine.runAndWait()

        if 'Nice' in query:
            engine.say('Absolutly sir')
            engine.runAndWait()

        if 'play music' in query:
            open_spotify(username = 'woo9l14m24zfhoxu8ogr546zd',
clientID = 'e97d5d276e8245018f89735856161ce2',
clientSecret = '5716b63696d3495787e0cb3d8e18bbb3',
redirect_uri = 'http://google.com/callback/')