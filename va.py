from lns import speak, get_audio
from functools import cache
import file
import wakeup
import pywhatkit
import wikipedia
import pomodoro
import datetime
import pyjokes


# This is the keyword that terminates the program
TERMINATE_WORD = 'goodbye'
# The response before termination.
TERMINATE_RESPONSE = 'Goodbye Sir. Have a nice day!'


@cache
def main():
    # This keeps Johnson up until the wake-up command is given.
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

        # Video is played on youtube when the 'play' command is given.
        elif 'play' in speech:
            video_title = speech.split('play')[-1]
            if video_title != '':
                speak(f'playing {video_title}')
                pywhatkit.playonyt(video_title)
            else:
                speak("What do you want me to play Sir?")

        # Wiki summaries are given when the 'who is' command is given
        elif 'who is' in speech:
            name = speech.split('who is')[-1]
            try:
                speak(wikipedia.summary(name))
            except:
                speak("Sorry I didn't get the name")

        # Goggle searches are initiated when 'Google' command is given.
        elif 'Google' in speech:
            word = speech.split('Google')[-1]
            if word != '':
                pywhatkit.search(word)
            else:
                speak("What do you want me to Google Sir?")

        # The pomodoro technique is initiated at the mention of 'start focus'.
        elif 'start focus' in speech.casefold():
            pomodoro.pomodoro()

        # Johnson gives the current time when 'time' is mentioned in a speech.
        elif 'time' in speech:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f'The time is {time}')

        # Johnson tells a joke when 'joke' is mentioned in the command.
        elif 'joke' in speech:
            joke = pyjokes.get_joke()
            speak(joke)

        elif wakeup.greetings(speech):
            wakeup.response(speech)

        else:
            speak("I don't understand")


if __name__ == '__main__':
    main()

