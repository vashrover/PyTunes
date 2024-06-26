from pygame import mixer 
from tkinter import Tk 
from tkinter import Label 
from tkinter import Button 
from tkinter import filedialog 
from tkinter.ttk import * 
from tkinter import * 
import os 
current_volume=float(0.5) 
song="a" 
#functions 
def play_song(): #to select the song 
    global song 
    filename= filedialog.askopenfilename(initialdir= "V:\PYmusic", title= "Please select a song") 
    current_song=filename 
    song_title=filename.split("/") 
    song_title=song_title[-1] 
    print(song_title) 
    song=str(os.path.basename(filename)) 
    try: 
        mixer.init() 
        mixer.music.load(current_song) 
        mixer.music.set_volume(current_volume) 
        mixer.music.play() 
        titlelabel.config(fg= "purple", text= "Now Playing : " + song) 
        volume_Label.config(fg= "purple", text= "Volume:" + 
        str(current_volume)) 
    except Exception as e: 
        print(e) 
        titlelabel.config(fg= "red", text= "Error Playing Track" ) 

def decrease_volume(): 
    try: 
        global current_volume 
        if current_volume<= 0: 
            volume_Label.config(fg= "Red", text= "Volume: Muted") 
            return 
        current_volume= current_volume- float(0.1) 
        current_volume= round(current_volume,1) 
        mixer.music.set_volume(current_volume) 
        volume_Label.config(fg= "green", text ="Volume:" + str(current_volume))
    except Exception as e: 
        print(e) 
        titlelabel.config(fg="red", text= "Track not selected") 

def increase_volume(): 
    try: 
        global current_volume 
        if current_volume>= 1: 
            volume_Label.config(fg= "Red", text= "Volume: Max") 
            return 
        current_volume= current_volume+ float(0.1) 
        current_volume= round(current_volume,1) 
        mixer.music.set_volume(current_volume) 
        volume_Label.config(fg= "green", text ="Volume:" + str(current_volume)) 
    except Exception as e: 
        print(e) 
        titlelabel.config(fg="red", text= "Track not selected") 

def pause_song(): 
    global song 
    try: 
        mixer.music.pause() 
        titlelabel.config(fg="purple", text="Paused:" + song) 
    except Exception as e: 
        print(e) 
        titlelabel.config(fg= "red", text= "Track not selected") 

def unpause_song(): 
    global song 
    try: 
        mixer.music.unpause() 
        titlelabel.config(fg="purple", text="Resumed:" + song) 
    except Exception as e: 
        print(e) 
        titlelabel.config(fg="red", text="Track not selected") 

def display_lyrics(): 
    global song 
    if(song!="a"): #if song name has changed to a filename 
        newWindow=Toplevel(master) 
        newWindow.configure(background="#D2AFFF") 
        newWindow.title("Lyrics") 
    if song=="Bored.mp3": 
        Label(newWindow,text="Givin' you what you're beggin' for\n Givin' you what you say I need\n I don't want any settled scores\n I just want you to set me free\n Givin' you what you're beggin' for\n Givin' you what you say I need \nSay I need\nI'm not afraid anymore\nWhat makes you sure you're all I need? \nForget about it\nWhen you walk out the door and leave me torn\nYou're teachin' me to live without it",font=("Georgia",10,"italic"),fg="yellow",background="#D2AFFF").grid(sticky = "N", row=0, padx= 120) 
    elif song=="Happier than ever.mp3": 
        Label(newWindow, text="I don't relate to you\n I don't relate to you, no\n 'Cause I'd never treat me this shitty\n You made me hate this city/n And I don't talk shit about you on the internet\n Never told anyone anything bad\n 'Cause that shit's embarrassing,\n you were my everything\n And all that you did was make me fuckin' sad",font=("Georgia",10,"italic"),fg="yellow",background="#D2AFFF").grid(sticky= "N", row=0, padx=120) 
    elif song=="Harleys in Hawai.mp3": 
        Label(newWindow, text="I'll be your baby, on a Sunday\nOh, why don't we get out of town?\nCall me your baby, catch the same wave\nOh, no, no, there's no slowin' down\nYou and I, I\n Ridin' Harleys in Hawaii-i-i\n I'm on the back, I'm holdin' tight, I\nWant you to take me for a ride, ride\n When I hula-hula, hula\n So good, you'll take me to the jeweler-jeweler, jeweler\n There's pink and purple in the sky-y-y\n We're ridin' Harleys in Hawaii-i-i",font=("Georgia",10,"italic"),fg="yellow",background="#D2AFFF").grid(sticky= "N", row=0, padx=120) 
    elif song=="Heat Waves.mp3": 
        Label(newWindow, text="Sometimes, all I think about is you\n Late nights in the middle of June\n Heat waves been faking me out\n Heat waves been faking me out\n Sometimes, all I think about is you\n Late nights in the middle of June\n Heat waves been faking me out\n Can't make you happier now",font=("Georgia",10,"italic"),fg="yellow",background="#D2AFFF").grid(sticky= "N", row=0, padx=120) 
    elif song=="Save room for us.mp3": 
        Label(newWindow, text= "And I know you've moved on\n She will never love you\n Oh, the way that I do \nNow I'm dancing solo (Solo)/n Slowly disappearing\n It still hurts when I see you with her\n Just save room for us\n (I know you feel it somewhere, somewhere)\n Just save room for us, I trust you'll come back to us someday\n (I know you feel it somewhere, somewhere)",font=("Georgia",10,"italic"),fg="yellow",background="#D2AFFF").grid(sticky= "N", row=0, padx=120) 
    elif song=="At my worst.mp3": 
        Label(newWindow, text= "Don't you worry\nI'll be there, whenever you want me\nI need somebody who can love me at my worst\nNo, I'm not perfect, but I hope you see my worth\n'Cause it's only you, nobody new, I put you first\nAnd for you, boy, I swear I'll do the worst",font=("Georgia",10,"italic"),fg="yellow",background="#D2AFFF").grid(sticky= "N", row=0, padx=120) 
    else: 
        titlelabel.config(fg="red",text="Track not selected") 


#mainscreen 
master = Tk() 
master.configure(background="#D2AFFF") 
master.title("Pytunes") 

#Labels 
Label(master,text= "PyTunes", font=("courier", 15,"bold"),background="#D2AFFF", fg= "black").grid(sticky= "N", row=0, padx= 120) 
Label(master, text= "~Select your Vibe~", font=("Georgia", 12,"italic"),background="#D2AFFF", fg= "Yellow").grid(sticky= "N", row=2) 
titlelabel= Label(master, font=("Calibri", 12),background="#D2AFFF") 
titlelabel.grid(stick = "N", row=4) 
volume_Label=Label(master, font=("Calibri", 12),background="#D2AFFF") 
volume_Label.grid(sticky= "N", row=6) 

#Buttons 
Button(master, text=" Select", font=("Calibri", 12), command= play_song).grid(row=3, sticky = "N") #select button 
Button(master, text=" Pause", font=("Calibri", 12), command= pause_song).grid(row=4, sticky = "E") #pause button 
Button(master, text=" Play", font=("Calibri", 12), command= unpause_song).grid(row=4, sticky = "W") #play button 
Button(master, text=" Volume+", font=("Calibri", 12),command= increase_volume).grid(row=6, sticky = "W") #volume increase button 
Button(master, text=" Volume-", font=("Calibri", 12), command= decrease_volume).grid(row=6, sticky = "E") #volume decrease button 
Button(master, text=" Lyrics", font=("Calibri", 12), command= display_lyrics).grid(row=7, sticky = "S") #display lyrics button 
master.mainloop()
