import os
import random
import inflect
import pyttsx3
import speech_recognition as sr
from send2trash import send2trash


def speak(speech):
    engine = pyttsx3.init()
    engine.say(speech)
    engine.runAndWait()


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ''

    try:
        said = r.recognize_google(audio)
        print(said)
    except Exception as e:
        print(e)

    return said


RESPONSES = ['how may I help you?', 'how can I help you?', "how may I be of service?"]

WAKE = 'hello Johnson'


def wake():
    while True:
        print("Listening...")
        speech = get_audio()
        if speech.count(WAKE) > 0:
            speak(f'Hello Sir, {random.choice(RESPONSES)}')
            break


GREETINGS = {
    'hello': 'Hello!',
    'how are you': "Better than I deserve",
    'who are you': "I am an AI created by Kwame",
    'your name': 'My name is Johnson',
    'goodbye': 'Goodbye Sir. Have a nice day!',
}


def greetings(speech):
    speak(GREETINGS[speech])


"""FILE SEARCH"""
FILE_KEYWORD = 'files'
FOLDER_LOCATIONS = {
    'downloads': r'C:\Users\Quame Junior\Downloads\Video',
    'videos': r'D:\VIDEOS'
}


def check(path):
    """ Returns files in folder path. """
    for folder, sub_folders, filenames in os.walk(path):
        for filename in filenames:
            yield filename


def find(path_1, path_2):
    """ Returns common files in two different paths and gives an option to delete. """
    dir_1 = list(check(path_1))
    dir_1.sort()
    dir_2 = list(check(path_2))
    dir_2.sort()
    files = []
    p = inflect.engine()
    if len(dir_1) <= len(dir_2):
        print(path_1)
        for file in dir_1:
            mx = len(dir_2)
            mn = 0
            while mn <= mx:
                index = (mx + mn)//2
                if file == dir_2[index]:
                    files.append(file)
                    break
                elif file < dir_2[index]:
                    mx = index - 1
                else:
                    mn = index + 1
    else:
        print(path_2)
        for file in dir_2:
            mx = len(dir_1)
            mn = 0
            while mn <= mx:
                index = (mx + mn)//2
                if file == dir_1[index]:
                    files.append(file)
                    break
                elif file < dir_1[index]:
                    mx = index - 1
                else:
                    mn = index + 1
    if len(files) == 0:
        speak("No files found Sir")
    else:
        speak(f"{len(files)} {p.plural_noun('file', len(files))} found\n")
        speech = get_audio()
        if 'what' in speech:
            speak(files)
        speak('Should I delete files Sir?')
        speech = get_audio()
        if speech.casefold() in ['yes', 'yeah']:
            speak("Deleting files")
            for f in files:
                filename = os.path.join(path_2, f)
                send2trash(filename)
            speak(f"{len(files)} {p.plural_noun('file',len(files))} deleted")
        elif speech.casefold() in ['no', 'nope', 'naah']:
            speak("Ok Sir")


def file_search(speech):
    path_1, path_2 = speech.split('and')
    for word in FOLDER_LOCATIONS:
        if word in path_1:
            path_1 = FOLDER_LOCATIONS[word]
        if word in path_2:
            path_2 = FOLDER_LOCATIONS[word]
    find(path_1, path_2)


def main():
    wake()
    while True:
        speech = get_audio()
        if speech in GREETINGS:
            if speech == 'goodbye':
                greetings(speech)
                break
            else:
                greetings(speech)
        elif FILE_KEYWORD in speech:
            file_search(speech)
            speak('Is there anything else I can help you with Sir?')
        elif 'thank you' in speech:
            speak("You're welcome")
        elif speech == '':
            continue
        else:
            speak("I don't understand")


if __name__ == '__main__':
    main()






