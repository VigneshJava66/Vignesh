import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes
import requests

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# speak("Welcome Sir, Here your AI assistant JARVIS to help you")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The Current time is")
    speak(Time)

def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The Current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome Sir, Here your AI assistant JARVIS to help you")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >=6 and hour <12:
        speak("Good Morning Sir!")
    elif hour >=12 and hour <18:
        speak("Good Afternoon Sir!")
    elif hour >=18 and hour <24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")

    speak("JARVIS at your Service. Please tell me, how may i help you Sir?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    
    except Exception as e:
        print(e)
        speak("Say that again Please...")


        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('vjvaliant59@gmail.com', 'vignesh$666')
    server.send_message('vjvaliant59@gmail.com', to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save('F:\\New folder\\ss.png')

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU Usage is at'+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif 'search in chrome' in query:
            speak("What should I Search?")
            chromepath = 'C:\Program Files\Google\Chrome\Application\chrome %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'log out' in query:
            os.system("shutdown -l")
        
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'play songs' in query:
            songs_dir = 'D:\Memory Card\Songs'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'note this' in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("you said me to remember that", data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()

        elif 'screenshot' in query:
            screenshot()
            speak("Done!")

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()

        elif 'offline' in query:
            speak("Going Offline")
            quit()


