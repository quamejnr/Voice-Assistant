from lns import speak, get_audio
import file
import wakeup


TERMINATE_WORD = 'goodbye'
TERMINATE_RESPONSE = 'Goodbye Sir. Have a nice day!'


def main():
    wakeup.wake()
    while True:
        speech = get_audio()
        if speech == '':
            continue
        elif speech.count(TERMINATE_WORD) > 0:
            speak(TERMINATE_RESPONSE)
            break
        elif speech in wakeup.GREETINGS:
            wakeup.greetings(speech)
        elif file.FILE_KEYWORD in speech:
            file.common(speech)
            speak('Is there anything else I can help you with Sir?')
            continue
        else:
            speak("I don't understand")


# TODO: Add functionality for va to tell what it is capable of


if __name__ == '__main__':
    main()







