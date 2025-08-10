import speech_recognition as sr
import pyttsx3
import datetime

def speak(text):
    engine = pyttsx3.init()
    # Set female voice
    voices = engine.getProperty('voices')
    for voice in voices:
        if 'female' in voice.name.lower() or 'zira' in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    engine.setProperty('rate', 175)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print(f'You said: {command}')
        return command.lower()
    except sr.UnknownValueError:
        speak('Sorry, I did not understand that.')
        return ''
    except sr.RequestError:
        speak('Sorry, my speech service is down.')
        return ''

def respond(command):
    if 'hello' in command or 'hi' in command:
        speak('Hello! How can I help you today?')
    elif 'time' in command:
        now = datetime.datetime.now().strftime('%I:%M %p')
        speak(f'The time is {now}')
    elif 'your name' in command:
        speak('My name is Rubi, your AI assistant!')
    elif 'exit' in command or 'quit' in command:
        speak('Goodbye!')
        exit()
    else:
        speak('Sorry, I can do only simple things for now.')

def main():
    speak('Hello, I am Rubi, your AI assistant!')
    while True:
        command = listen()
        if command:
            respond(command)

if __name__ == '__main__':
    main()
