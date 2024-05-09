import speech_recognition as sr
import pyttsx3
import time

# Initialize the recognizer object
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Define a function to convert text to speech
def respond(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to recognize speech from the microphone
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source, phrase_time_limit=10)
        try:
            text = r.recognize_google(audio)
            print("You said: " + text)
            return text
        except:
            print("Sorry could not recognize what you said")
            return listen()

# Define a function to check if the voice is valid or not
def check_voice(text):
    valid_voice = ["I me and myself"]
    if text.lower() in valid_voice:
        return True
    else:
        return False

# Listen for voice input and check if it's valid
text = listen()
if check_voice(text):
    print("Your password is valid!")
    respond("Your password is valid!")
else:
    print("Your password is not valid!")
    respond("Your password is not valid!")
