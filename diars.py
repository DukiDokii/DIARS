import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

r = sr.Recognizer()
with sr.Microphone() as source:
    print ("Listening...")
    r.pause_threshold = 1
    audio = r.listen(source)

engine = pyttsx3.init()

wake_word = "Doki"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def open_website(url):
    webbrowser.open(url)
    speak("Opening website, sir.")

def tell_time():
    time = datetime.datetime.now().strfttime("%I:%M %p")
    speak(f'The time is {time}, sir.')

if wake_word in r.recognize_google(audio):
    speak("Yes, sir?")

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:" + command)

        if "open" in command:
            if "website" in command:
                url = command.split()[-1]
                open_website(url)
            else:
                speak("I'm not sure what you want me to open.")
        elif "time" in command:
            tell_time()
        else:
            speak("I'm sorry, I didn't understand that.")

    except sr.UnknownValueError:
        speak("I'm sorry, I didnt understand that.")
    except sr.RequestError as e:
        speak("Sorry, I couldn't reach the google servers. Check your internet connection")