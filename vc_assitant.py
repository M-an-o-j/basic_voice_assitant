import speech_recognition as sr
from gtts import gTTS
import os

def speak(text):
    """Play a given text as speech.
    
    This function uses the gTTS (Google Text-to-Speech) library to convert
    the given text into an mp3 file, and then plays it using the default
    media player on the system.
    
    Parameters:
        text (str): The text to be spoken.
    
    """
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    os.system("start response.mp3")  # Use 'afplay' on macOS or 'xdg-open' on Linux

def listen():
    """Listen for speech input and return the text of what was said.
    
    This function uses the SpeechRecognition library to listen for
    speech input, and then returns the text of what was said. If
    the speech recognition service could not understand what was said,
    or if the request to the service failed, this function will print
    an appropriate error message and return an empty string.
    
    Returns:
        str: The text of what was said.
    
    """
    
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
