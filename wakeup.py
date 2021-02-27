from lns import speak, get_audio
import random
from functools import cache


# This is the command that wakes Johnson up for other commands.
WAKE = 'hello Johnson'
# These are different responses Johnson can give.
WAKE_RESPONSES = ['how may I help you?', 'how can I help you?', "how may I be of service?"]


def wake():
    while True:
        # Johnson waits for the wake command.
        print("Listening...")
        speech = get_audio()
        # Checks if the wake command is mentioned in the speech.
        if speech.count(WAKE) > 0:
            # Johnson responds with one of the wake responses chosen randomly
            # and is initialized for other commands when it hears the wake command.
            speak(f'Hello {random.choice(WAKE_RESPONSES)}')
            break


# These are some commands and responses to those commands.
GREETINGS = {
    'hello': 'Hello!',
    'hi': 'Hi!',
    'how are you': "I don't know how I feel, I don't quite have feelings.",
    'who are you': "I am an AI created by Kwame.",
    'your name': 'My name is Johnson.',
    'can you do': 'I can play songs on youtube, make google searches, tell you the time, '
                  'search for files and set a timer for you.',
    'where are you': "I am nowhere, but everywhere."

}


@cache
def greetings(speech):
    for i in GREETINGS.keys():
        # Checks if any of the words in the GREETINGS dictionary is mentioned.
        if speech.count(i) > 0:
            return True


@cache
def response(speech):
    for i in GREETINGS.keys():
        # Checks if any of the words in the GREETINGS dictionary is mentioned
        # and gives appropriate response.
        if speech.count(i) > 0:
            speak(GREETINGS[i])

