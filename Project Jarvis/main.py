import speech_recognition as sr
import webbrowser
import pyttsx3
import time                   #Used here to add delay (sleep)
import musiclibrary

def speak(text):
    engine = pyttsx3.init()   
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def work(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")    
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com") 
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]

        if song in musiclibrary.music:
            link = musiclibrary.music[song]
            webbrowser.open(link)
        else:
            speak("Sorry, song not found")
    
if __name__ == "__main__":
    speak("I am active")

    r = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
                #timeout=2(wait for 2 sec)  ,  phrase_time_limit=2(listion speech for 2 sec)

            word = r.recognize_google(audio).lower()
            print("You said:", word)

            if "jarvis" in word:
                time.sleep(0.3)   
                speak("yess boss")

                with sr.Microphone() as source:
                    print("jarvis in action..")
                    r.adjust_for_ambient_noise(source, duration=1)
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    command = r.recognize_google(audio).lower()
                    work(command)
                    print(command) 

        except Exception as e:
            print("Error:", e)
