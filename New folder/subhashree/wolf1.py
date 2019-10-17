import pyttsx3
import datetime
import speech_recognition as sr
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Choonulu. Baaaboo Please tell me how may I help you")
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listineing..........')
        r.pause_threshold=0.81
        audio = r.listen(source)
    try:
        print("Recognising......")
        query= r.recognize_google(audio,language='en-in')
        print(f'user said {query}\n')
    except Exception as e:
        speak("sorry I don\'t Know")
        return 'none'
    return query


if __name__=='__main__':
    wishMe()
    takecommand()
