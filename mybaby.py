import datetime
import pyttsx3
import speech_recognition as sr


def take_commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print('Recognizing ...')
            query = r.recognize_google(audio, language='en-in')
            print('voice recognized is : ', query)
        except Exception as e:
            print(e)
            print("sorry i can't understand ")
            return None
    return query


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()


def tellday():
    day = datetime.datetime.today().weekday()
    days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

    if day in days.keys():
        weekday = days[day]
        print(weekday)
        speak('today is  '+weekday)


speak('hiiiiii')
speak('hi baby')
command = take_commands()
speak('love you too baby...')
if 'day' in command:
    tellday()




