import pyttsx3
import speech_recognition as sr


def speak(speech):
    engine = pyttsx3.init()
    engine.say(speech)
    engine.runAndWait()


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # Voice assistant listens via the microphone.
        audio = r.listen(source)
        said = ''

    try:
        # Speech recognition is then used to understand what was said.
        said = r.recognize_google(audio)
        print(said)
    except Exception as e:
        print(e)

    return said
