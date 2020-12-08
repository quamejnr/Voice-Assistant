import os
import inflect
from send2trash import send2trash
from lns import speak, get_audio
from functools import cache


FILE_KEYWORD = 'files'
FOLDER_LOCATIONS = {
    'downloads': r'C:\Users\Quame Junior\Downloads\Video',
    'videos': r'D:\VIDEOS',
    'books': r'D:\BOOKS\My Collection',
    'movies': r'D:\VIDEOS\CINEMA',
}


def check(path):
    """ Returns files in folder path. """
    for folder, sub_folders, filenames in os.walk(path):
        for filename in filenames:
            yield filename


@cache
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
        print(files)
        while True:
            speak('Should I delete files Sir?')
            speech = get_audio()
            if speech == '':
                continue
            else:
                break
        if speech.casefold() in ['yes', 'yeah']:
            speak("Deleting files")
            for f in files:
                filename = os.path.join(path_2, f)
                send2trash(filename)
            speak(f"{len(files)} {p.plural_noun('file',len(files))} deleted")
        elif speech.casefold() in ['no', 'nope', 'naah']:
            speak("Ok Sir")


def common(speech):
    path_1, path_2 = speech.split('and')
    for word in FOLDER_LOCATIONS:
        if word in path_1:
            path_1 = FOLDER_LOCATIONS[word]
        if word in path_2:
            path_2 = FOLDER_LOCATIONS[word]
    find(path_1, path_2)


def search(path, keyword=''):
    """ Search for files in a path with keyword. """
    dir_list = os.listdir(path)
    dir_list.sort()
    for f in dir_list:
        fullname = os.path.join(path, f)
        if os.path.isdir(fullname):
            search(fullname, keyword)
        else:
            if keyword.casefold() in f.casefold():
                print(f)

    # TODO: Modify search functionality and add to voice-assistant
