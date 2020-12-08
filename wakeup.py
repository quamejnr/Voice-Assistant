from lns import speak, get_audio
import random
from functools import cache

WAKE = 'hello Johnson'
WAKE_RESPONSES = ['how may I help you?', 'how can I help you?', "how may I be of service?"]


def wake():
    while True:
        print("Listening...")
        speech = get_audio()
        if speech.count(WAKE) > 0:
            speak(f'Hello Sir, {random.choice(WAKE_RESPONSES)}')
            break


GREETINGS = {
    'hello': 'Hello!',
    'hi': 'Hi!',
    'how are you': "Better than I deserve",
    'who are you': "I am an AI created by Kwame",
    'your name': 'My name is Johnson',
    'can you do': 'I can play songs on youtube, make google searches, tell you the time, '
                  'search for files and set a timer for you',

}


@cache
def greetings(speech):
    for i in GREETINGS.keys():
        if speech.count(i) > 0:
            return True


@cache
def response(speech):
    for i in GREETINGS.keys():
        if speech.count(i) > 0:
            speak(GREETINGS[i])
