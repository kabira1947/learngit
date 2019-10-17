import pyaudio

from pydub import AudioSegment

import pandas as pd

from gtts import gTTS

def text_speech(text,filename):
    pass
def mergeaudio(audio):
    pass
def generateSkeleton():
    # krupaya dhyan dijiye
    audio=AudioSegment.from_mp3("railway.mp3")
    start= 88000
    end= 90200
    audioprocess=audio[start:end]
    audioprocess.export("krupaya dhyan de.mp3", format="mp3")

    # jahan se jane wali hai


    # se chalkar
    start = 91000
    end = 92200
    audioprocess = audio[start:end]
    audioprocess.export("se-chalkar.mp3", format="mp3")
    #via city


    #ke raaste
    audio = AudioSegment.from_mp3("railway.mp3")
    start = 94000
    end = 95000
    audioprocess = audio[start:end]
    audioprocess.export("ke raaste.mp3", format="mp3")

    # to city


    # ko jane wali gadi sankhya
    audio = AudioSegment.from_mp3("railway.mp3")
    start = 96000
    end = 98900
    audioprocess = audio[start:end]
    audioprocess.export("gadi sankhya.mp3", format="mp3")

    # train num and name

    # kuch hi samay mai platform
    audio = AudioSegment.from_mp3("railway.mp3")
    start = 105000
    end = 108200
    audioprocess = audio[start:end]
    audioprocess.export("kuch hi samay mai.mp3", format="mp3")
    #platform number
    #par aa rahi hai
    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export("par aa rahi hai.mp3", format="mp3")

def generate_announcement(filename):
    exeldata=pd.read_excel(filename)
    for index, items in exeldata.iterrows():
        #from city
        text_speech(item['from'],"fcity.mp3")
        #via city
        text_speech(item['via'], "via.mp3")
        #to city
        text_speech(item['to'], "to.mp3")
        #number and name
        text_speech(item['tnum']+" " +item['tname'], "tnamenum.mp3")
        #platform number
        text_speech(item['platform'], "platform.mp3")

if __name__ == '__main__':
    print("generating Skeleton")
    generateSkeleton()
    print("Now Generating Announcement")
    generate_announcement("announce_hindi.xlsx")