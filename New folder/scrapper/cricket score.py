import tkinter
import json
import requests
import time
root = tkinter.Tk()
root.geometry("500x400")
match_data=requests.get("https://cricapi.com/api/cricketScore?apikey=wbciJlzzm2PTNP7vLutVwZaBYSf1&unique_id=1034809")
jason_data=match_data.json()

def times():
    current_score=jason_data['stat']
    score.configure(text="Current_score: " + current_score)
    score.after(200,times)




score=tkinter.Label(root,font=("time",15,"bold"),bg="white")
score.grid(row=2,column=2,pady=25,padx=100)
times()

root.mainloop()