import speech_recognition as sr
from gtts import gTTS
import os

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    os.system("start response.mp3")  # Use 'afplay' on macOS or 'xdg-open' on Linux

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            print("Could not request results from the speech recognition service.")
            return ""

def main():
    while True:
        command = listen()
        if 'stop' in command:
            speak("Goodbye!")
            break
        elif 'hello' in command:
            speak("Hello! How can I help you today?")
        # Add more commands as needed

if __name__ == "__main__":
    main()
