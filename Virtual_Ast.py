import pyttsx3              #pip install pyttsx3
import speech_recognition as sp         #pip install speechRecognition
import datetime as dt
import wikipedia        #pip install wikipedia
import webbrowser
import os
import smtplib

designer = "Swayam"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def wishMe():  
    hr = int(dt.datetime.now().hour)
    mn = int(dt.datetime.now().minute)
    if (hr>=0 and hr<12):
        speak("Good Morning"+ designer)
    elif (hr>=12 and hr<18):
        speak("Good Afternoon"+ designer)
    else:
        speak("Good Evening"+ designer)
    speak("I am your Virtual Assistant.....How can I help you?")

def Listen():
    r = sp.Recognizer()
    with sp.Microphone() as input_data:
        print("Listening......")
        audio = r.listen (input_data)
    data=''
    try:
        data = r.recognize_google(audio)
        print("You said -  "+ data)
        # query = r.recognize_google(audio, Language='en-in')
        # print("user said :",query)
    except sp.UnknownValueError : 
        print("Say that again please")
    except sp.RequestError as e:
        print("error "+ e)
    # return query
    return data


def main():
    speak("Initialising your Virtual Assistant")
    wishMe()
    res = Listen()

    if 'wikipedia'  in res.lower():
        speak("Searching for results")
        res = res.replace("wikipedia", "")
        result =   wikipedia.summary(res, sentences = 2)
        print(result)
        speak(result)
    elif 'open youtube' in res.lower(): 
        webbrowser.open("youtube.com")
    elif 'open google' in res.lower():
        webbrowser.open("google.com")
    elif 'play music' in res.lower():
        s_dir="C:\\Users\\lenovo\\AppData\\Local\\Microsoft\\WindowsApps\\SpotifyAB.SpotifyMusic_zpdnekdrzrea0"
        songs=os.listdir(s_dir)
        os.startfile(os.path.join(s_dir,songs[0]))
   
main()
    






