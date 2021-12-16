import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import requests
from bs4 import BeautifulSoup



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
            engine.say(text)
            engine.runAndWait()
def wishMe():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12:
        talk('Hello,Good Morning. How can I help you')
        print('hello,Good Morning. How can I help you')
    elif hour>=12 and hour<18:
        talk('Hello, Good Afternoon. How can I help you')
        print('Hello, Good Afternoon. How can I help you')
    else:
        talk('Hello,Good Evening. How can I help you')
        print('Hello,good Evening. How can I help you')
def take_command():
    try:
        with sr .Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)

    except:
        pass
    return command
print('loading your AI personal assistant')
talk('loading your AI personal assistant')
wishMe()

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'date and time' in command:
        now = datetime.datetime.now()
        print('current date and time : ')
        p=now.strftime('%Y-%m-%d %I %M %p')
        talk(p)

    elif 'who ' in command:
        person = command.replace('who is ', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'temperature' in command:
        search = 'temperature in kerala'
        url = f'https://www.google.com/search?q={search}'
        r = requests.get(url)
        data = BeautifulSoup(r.text, 'html.parser')
        temp = data.find('div', class_='BNeawe').text
        print(temp)
        talk(f'current {search} is {temp}')

    else:
        talk('Please say the command again.')



while True:
    run_alexa()

