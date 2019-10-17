import wolframalpha as w
import wikipedia
import webbrowser
import random
import sys
import datetime
#import smtplib
import speech_recognition as sr
import pyttsx3

client=w.Client('J6JJT6-R2TW44EY3H')

search = pyttsx3.init('sapi5')
voices=search.getProperty('voices')
#print(voices[1].id)
search.setProperty('voice', voices[0].id)


def speak(audio):
    print('Chuunuuluu: ' + audio)
    search.say(audio)
    search.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour >=5 and hour<=12:
        speak('Good Morning Baabuu!')
    elif hour>12 and  hour<13:
        speak("Good Noon Baabuu!")
    elif hour >13 and hour<16:
        speak("Good After Noon")
    elif hour>16 and hour<19:
        speak("Good Evening Baabuu!")
    elif hour>17 and hour< 22:
        speak("Hello Baabu!")
    elif hour >22 and hour<23:
        speak("Have Your Dinner? ")
        if 'no' or 'naaa' or 'nai' in query:
            speak('Cool That is my Princess')
        else:
            speak('Go and have your dinner Otherwise do not talk to me. I am not listening!')
    else:
        speak("getting Late Go To Sleep Baabuu!")
    speak("I am Chunulu, Your Baabuu Assigned me to assist You  your Highness, How may I help You Princess? ")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Soo-noocchhi ! ..   kuhana please!")
        #r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=2)
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        print('Baboo: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Sorry Baaboo! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query


'''def sendmail(to, text):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, text)
    server.close()
'''

if __name__== "__main__":
    wishme()
    while True:

        query = takecommand()
        query = query.lower()

        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')
        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')
        elif 'open g-mail' in query or 'e mail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')
        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy',
                      'I love you Princess' ]
            speak(random.choice(stMsgs))
        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "yourmailid@gmail.com"
                #sendmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my Princess. I am not able to send this email")

        elif 'nothing' in query or 'abort' in query or 'stop' in query:
                speak('okay')
                speak('Bye Princess, have a good day.')
                sys.exit()
        elif 'hello' in query:
                speak('Hello Sir')
        elif 'bye' in query:
                speak('Bye Princess, have a good day.')
                sys.exit()


        else:
            speak('Dekhucchi..')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('Choonoolooo Mote - ')
                    speak('Miligala')
                    speak(results)


                except:
                    results = wikipedia.summary(query, sentences=6)
                    speak('FIND SOMETHING!')
                    speak("According to My Database")
                    print(results)
                    speak(results)


            except:
                webbrowser.open('www.google.com')
        speak('Next Command! Babu!')