import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import openai
import wikipedia
import pyaudio

# Text to Speech
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


# Speech to text
def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio , language="en-in")    
            print(f"User Said {query}")
            return query
        except Exception as e:
            return "Sorry an Error occur"
            
if __name__ == '__main__':
    # print("Pycharm")
    say("Hello, I am Jarvis A.I. How can I help you ")
    while True:
        print("Listening....")
        query = takecommand()

        #query for opening sites

        sites = [["youtube" , "www.youtube.com"],["facebook" , "www.facebook.com"],["instagram" , "www.instagram.com"],["gmail" , "www.gmail.com"],["netflix" , "www.netflix.com"],["snapchat" , "www.snapchat.com"],["twitter" , "www.twitter.com"],["chat g.p.t" , "www.chat.openai.com"]]
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                webbrowser.open(site[1])
                say(f"Opening {site[0]} ")

            if "play music".lower() in query.lower():
                musicpath = "C:\\Users\\Muhammad Adan\\Downloads\\eid final.wav"
                os.startfile(musicpath)

            if "the time".lower() in query.lower():
                strftime = datetime.datetime.now().strftime("%H:%M")
                say(f"Sir the time is {strftime}") 

        # query for opening desktop applications
        applications = [["spotify" , "C:\\Users\Muhammad Adan\\AppData\\Local\\Microsoft\\WindowsApps\\Spotify.exe"],["notepad" , "C:\\Windows\\system32\\notepad.exe"],["v.s code" , "C:\\Users\\Muhammad Adan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"],["google chrome" , "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"],["brave" , "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"],["valorant" , "C:\\Riot Games\\Riot Client\\RiotClientServices.exe"]]
        for app in applications:
            if f"open {app[0]}".lower() in query.lower():
                os.startfile(app[1])
                say(f"Opening {app[0]} ")

