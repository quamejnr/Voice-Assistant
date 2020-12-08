from lns import speak, get_audio
import file
import wakeup
import pywhatkit
import wikipedia
import pomodoro
import datetime
from functools import cache


TERMINATE_WORD = 'goodbye'
TERMINATE_RESPONSE = 'Goodbye Sir. Have a nice day!'


@cache
def main():
    wakeup.wake()
    while True:
        speech = get_audio()
        if speech == '':
            continue
        elif speech.count(TERMINATE_WORD) > 0:
            speak(TERMINATE_RESPONSE)
            break
        elif file.FILE_KEYWORD in speech:
            file.common(speech)
        elif 'play' in speech:
            video_title = speech.split('play')[-1]
            if video_title != '':
                speak(f'playing {video_title}')
                pywhatkit.playonyt(video_title)
            else:
                speak("What do you want me to play Sir?")
        elif 'who is' in speech:
            name = speech.split('who is')[-1]
            try:
                speak(wikipedia.summary(name))
            except:
                speak("Sorry I didn't get the name")
        elif 'Google' in speech:
            word = speech.split('Google')[-1]
            if word != '':
                pywhatkit.search(word)
            else:
                speak("What do you want me to Google Sir?")
        elif 'start focus' in speech.casefold():
            pomodoro.pomodoro()
        elif 'time' in speech:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f'The time is {time}')
        elif wakeup.greetings(speech):
            wakeup.response(speech)
        else:
            speak("I don't understand")


if __name__ == '__main__':
    main()



