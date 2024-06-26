import pygame
from pygame import mixer  
from tkinter import Tk 
from tkinter import Label 
from tkinter import Button 
from tkinter import filedialog, PhotoImage, Toplevel, Canvas
from tkinter.ttk import * 
from tkinter import * 
from tkinterdnd2 import TkinterDnD, DND_FILES
import os 
from PIL import Image, ImageTk
import threading
import time


#global variables
current_volume=0.5
song="a" 
is_playing=False    #to track play/pause state
file_path=None
length=0            #length of the music
filename=None


#functions 
def play_song():    #to initialize the mixer and play the sonng
    global song, is_playing,length,file_path,filename,seekbar_position
    
    if filename:
        filename = file_path.strip('{}')
        current_song=filename 
        song_title=filename.split("/") 
        song_title=song_title[-1] 
        song=str(os.path.basename(filename)) 
        file_path=filename
    try: 
        mixer.init() 
        mixer.music.load(current_song) 
        mixer.music.set_volume(current_volume) 
        mixer.music.play() 
        is_playing = True
        length=(pygame.mixer.Sound(file_path).get_length())
        seekbar_position=585/length
        update_play_pause_button()
        canvas.itemconfig(title_label_id,fill="#32022D", text="Now Playing: "+song)
 
        canvas.itemconfig(volume_label_id,fill="#32022D", text ="Volume: " + str(int(current_volume*10)))

    except Exception as e: 
        print(e) 
        canvas.itemconfig(title_label_id,fill="red", text="Error Playing Track")

def decrease_volume():              #to decrease vol
    global current_volume
    try:  
        if(current_volume>0):
            current_volume= current_volume- 0.1
        elif(current_volume== 0):
            canvas.itemconfig(volume_label_id,fill="#32022D", text="Volume: Muted")
            return 
        current_volume= round(current_volume,1) 
        mixer.music.set_volume(current_volume) 
        canvas.itemconfig(volume_label_id, fill="#32022D", text ="Volume: " + str(int(current_volume*10)))
    except Exception as e: 
        print(e) 
        canvas.itemconfig(title_label_id, fill="red", text= "Track not selected") 

def increase_volume():          #to increase vol
    try: 
        global current_volume 
        if current_volume>= 1: 
            canvas.itemconfig(volume_label_id,fill= "Red", text= "Volume: Max") 
            return 
        current_volume= current_volume+ 0.1 
        current_volume= round(current_volume,1) 
        mixer.music.set_volume(current_volume) 
        canvas.itemconfig(volume_label_id,fill="#32022D", text ="Volume: " + str(int(current_volume*10))) 
    except Exception as e: 
        print(e) 
        canvas.itemconfig(title_label_id,fill="red", text= "Track not selected") 

def toggle_play_pause():            #play pause buttton
    global song, is_playing
    try: 
        if is_playing:
            mixer.music.pause() 
            canvas.itemconfig(title_label_id,fill="#32022D", text="Paused: " + song) 
        else:
            mixer.music.unpause()
            canvas.itemconfig(title_label_id,fill="#32022D", text="Resumed: " + song)
        is_playing = not is_playing
        update_play_pause_button()
    except Exception as e: 
        print(e) 
        canvas.itemconfig(title_label_id,fill= "red", text= "Track not selected") 

def update_play_pause_button():
    canvas.itemconfig(play_pause_button,image=pause_img if is_playing else play_img)

def drop(event):            #drag and drop functionality
    try:
        global file_path,filename
        file_path = event.data
        filename=file_path
        play_song()
    except Exception as e:
        canvas.itemconfig(title_label_id,fill= "red", text= "Invalid Format")
   

def load_image(image_path,x=60,y=60):
    img = Image.open(image_path)
    img = img.resize((x, y))  
    return ImageTk.PhotoImage(img)

def move_knob(event): 
    try:          #to move the seekbar knob
        x = event.x
        if 105 <= x <= 690:  # Limit the knob movement
            canvas.coords(knob, x, 350)
            qoutient=(x - 5) / 700
            new_pos = qoutient*length
            mixer.music.pause()
            mixer.music.play(start=new_pos)
    except Exception as e:
        canvas.itemconfig(title_label_id,fill= "red", text= "Track not selected")


def choose_file():              #to choose music file
    global file_path,filename
    try:
        filename= filedialog.askopenfilename(initialdir= "Pytunes/", title= "Please select a song")
        file_path=filename
        play_song()
    except Exception as e: 
        print(e) 
        canvas.itemconfig(title_label_id,fill= "red", text= "Invalid Format") 



def show_dialog(event):     #theme button dialog box
    dropdown = Menu(master, tearoff=0)

    items = [
        {"label": "1","icon": "images/bg4.jpg"},
        {"label":"2","icon": "images/bg2.jpg"},
        {"label":"3","icon": "images/bg3.jpg"},
        {"label":"4","icon": "images/bg1.gif"}
    ]
    image_references = []
    for item in items:
     
        icon = Image.open(item["icon"])
        icon = icon.resize((120, 67))  
        icon = ImageTk.PhotoImage(icon)
        dropdown.add_command(image=icon, command=lambda text=item["label"]:theme_choose(text))
        image_references.append(icon)
    dropdown.image_references = image_references

    dropdown.post(event.x_root, event.y_root)

def theme_choose(color):        #theme button
    if(color=='1'):
        canvas.itemconfig(bg_label, image=bg_img)
    elif(color=='2'):
        canvas.itemconfig(bg_label, image=bg2)
    elif(color=='3'):
        canvas.itemconfig(bg_label, image=bg3)
    else:
        canvas.itemconfig(bg_label, image=bg4)

def restart_song():     #previous button
    global song, is_playing
    try: 
        if is_playing:
            mixer.music.set_pos(0) 
    except Exception as e: 
        print(e) 
        canvas.itemconfig(title_label_id,fill= "red", text= "Track not selected")      

def skip_duration():    #next button
    global song, is_playing
    try:
        if is_playing:
            mixer.music.play(start=mixer.music.get_pos()/1000+30)
    except Exception as e:
        print(e)
        canvas.itemconfig(title_label_id,fill= "red", text= "Track not selected")

def show_credits(master):
    credits_window = Toplevel()
    credits_window.title("Credits")
    credits_window.geometry("500x300")
    credits_window.config(cursor="@{}".format(cursor_img))
    credits_window.iconbitmap("images/11.ico")
    credits_canvas = Canvas(credits_window, width=500, height=300,background="#64035a")
    credits_canvas.pack(fill="both", expand=True)
    credits_window.resizable(False,False)
    credits_window.attributes('-alpha',0.9)
    bg_image_tk = load_image("images/girl.jpg",450,270)
    credits_canvas.create_image(250,150,image=bg_image_tk, anchor=CENTER)
    credits_text = """
    Credits:
    - Developer: Vashita Grover
    - Github: vashrover
    - Picture Reference: Pinterest
    """ 
    credits_canvas.image = bg_image_tk
    label = Label(credits_window, text=credits_text, font=("Georgia", 7),background="#64035a",fg="white",justify="left")
    label.place(relx=0.05, rely=0.7)
    credits_window.mainloop()

def close_credits_window(window):
    window.destroy() 



#mainscreen 
master = TkinterDnD.Tk() 
master.title("Pytunes") 
master.geometry("800x450")
master.resizable(False, False)
master.iconbitmap("images/11.ico")

cursor_img="images/11.cur"
master.config(cursor="@{}".format(cursor_img))

#Images
play_img = load_image("images/play.png")
pause_img = load_image("images/pause.png")
next_img=load_image("images/next.png")
prev_img=load_image("images/prev.png")
seekbar_bg_img = load_image("images/seekbar_bg.png", 600, 60)
knob_img = load_image("images/knob.png", 20, 20)
bg_img = load_image("images/bg4.jpg",800,450)
bg2 = load_image("images/bg2.jpg",800,450)
bg3 = load_image("images/bg3.jpg",800,450)
bg4 = load_image("images/bg1.gif",800,450)
up=load_image("images/up.png")
down=load_image("images/down.png")
theme_img=load_image("images/theme.png")
queue_img=load_image("images/queue.png")
logo_img=load_image("images/logo.png",400,325)

# Create the main canvas
canvas = Canvas(master, width=800, height=600)
canvas.pack(fill="both", expand=True)

# Set background image
bg_label = canvas.create_image(0, 0, anchor="nw", image=bg_img)

# Create text labels
#canvas.create_text(400, 50, text="~PyTunes~", font=("Georgia", 42, "italic"), fill="black")
canvas.create_image(400, 85, anchor="center", image=logo_img)
#canvas.create_text(400, 100, text="Music Player", font=("Courier", 20, "bold"), fill="black")

title_label_id= canvas.create_text(400, 235, text="", font=("Georgia", 16,"bold"),width="600")
volume_label_id = canvas.create_text(400, 315, text="", font=("Georgia", 16,"bold"))


# Create seekbar and knob on the canvas
seekbar = canvas.create_image(400, 350, anchor="center", image=seekbar_bg_img)
knob = canvas.create_image(110, 350, anchor="center", image=knob_img)
canvas.tag_bind(knob, "<B1-Motion>", move_knob)


# Button styles
button_style = {"font": ("Calibri", 14), "bg": "white", "fg": "black", "activebackground": "purple", "activeforeground": "white", "bd": 1}

# Create buttons
select_button = Button(master, text="Select",  **button_style)
canvas.create_window(400, 180, window=select_button, anchor="center")
select_button.bind("<Button-1>", lambda e: choose_file())

decrease_vol_button= canvas.create_image(240, 400, anchor="center", image=down)
canvas.tag_bind(decrease_vol_button, "<Button-1>", lambda e: decrease_volume())

theme_button = canvas.create_image(160, 400, anchor="center", image=theme_img)
canvas.tag_bind(theme_button, "<Button-1>",show_dialog)

prev_button = canvas.create_image(320, 400, anchor="center", image=prev_img)
canvas.tag_bind(prev_button, "<Button-1>", lambda e:restart_song())

play_pause_button = canvas.create_image(400, 400, anchor="center", image=play_img)
canvas.tag_bind(play_pause_button, "<Button-1>", lambda e: toggle_play_pause())

next_button = canvas.create_image(480, 400, anchor="center", image=next_img)
canvas.tag_bind(next_button, "<Button-1>", lambda e: skip_duration())

credits = canvas.create_image(640, 400, anchor="center", image=queue_img)
canvas.tag_bind(credits, "<Button-1>",lambda e: show_credits(master))

increase_vol_button = canvas.create_image(560, 400, anchor="center", image=up)
canvas.tag_bind(increase_vol_button, "<Button-1>", lambda e: increase_volume())



#drag and drop
master.drop_target_register(DND_FILES)
master.dnd_bind('<<Drop>>',drop)

master.mainloop()
