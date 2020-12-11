import time
from lns import get_audio, speak


def timer(minutes):

    """ Function to implement a timer. """

    tim = 0
    while tim != minutes:
        time.sleep(60)
        tim += 1
    return tim


def pomodoro():

    """
    Function that implements the pomodoro technique in which one focuses
    for a while with intermittent breaks

    """

    answers = ['yes', 'ok', 'sure', 'yh', 'yeah']

    speak("Do you want to start focus Sir?")
    while True:
        response = get_audio()
        if response == '':
            speak("I didn't hear you Sir")
        else:
            break
    if response in answers:
        focus_time = int(input("Focus time: "))
        break_time = int(input("Break time: "))
        while True:
            speak("Do you want to begin?")
            focus_response = get_audio()
            if focus_response in answers:
                speak("Beginning focus")
                focus = timer(focus_time)
                speak(f'Your {focus} minutes is up Sir')
                speak("Do you want to take a break?")
                break_response = get_audio()
                if break_response not in answers:
                    continue
                else:
                    timer(break_time)
                    speak("Break over Sir. Do you want to focus again?")
                    final_response = get_audio()
                    if final_response in answers:
                        continue
            break
