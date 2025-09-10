import speech_recognition as sr
import webbrowser
import pyaudio
import pyttsx3
import time
import musicLibrary
from news import headlines
from gemini import neerajai


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def proceesscommand(c):
    if "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkdin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open google" in c.lower():
        webbrowser.open("https://google.com")
    
    elif c.lower().startswith("play"):
        mic = c.lower().replace("play","",1).strip()
        if mic in musicLibrary.music:
            link = musicLibrary.music[mic]
            webbrowser.open(link)

    elif c.lower().endswith("news"):
        reports = c.lower().replace("news","",1).strip()
        a = headlines(reports)
        speak(a)
    else:
        data = c.lower()  
        theory = neerajai(data)
        print(theory)
        speak(theory)


if __name__=="__main__":
    speak("Hey Bro, how may I help you?")
    while True:
        r = sr.Recognizer()
        print("Initializing...")  
        try:
            with sr.Microphone() as source:
                print("Say something!")
                r.adjust_for_ambient_noise(source, duration=1)
                print("Energy threshold is set to:", r.energy_threshold)
                audio = r.listen(source, timeout=4, phrase_time_limit=10)

            voice = r.recognize_google(audio)

            if "hey bro" in voice.lower():
                speak("Yes bro")
                time.sleep(0.5)
                with sr.Microphone() as source:
                    speak("Bro got Activated")
                    print("Started")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)   

                    if "stop" in command.lower():
                        speak("Bro is shutting down")
                        break   

                    proceesscommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio")

        except sr.RequestError as e:
            print(f"Request Error: {e}")
