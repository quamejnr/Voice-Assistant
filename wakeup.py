from lns import speak, get_audio
import random

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
    'how are you': "Better than I deserve",
    'who are you': "I am an AI created by Kwame",
    'your name': 'My name is Johnson',

}


def greetings(speech):
    speak(GREETINGS[speech])

