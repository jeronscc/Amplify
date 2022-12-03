from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer     
import os
from PIL import ImageTk, Image

#Pop-up Window
root=tk.Tk()
root.title('Amplify')
root.geometry("350x640+650+55")
root.configure(bg= "#191414")
root.resizable(False,False)

mixer.init()

def openFolder():
    directory = filedialog.askdirectory()
    if directory:
        os.chdir(directory)
        music = os.listdir(directory)
        print(music)

        for song in music:
            if song.endswith(".mp3"):
                playlist.insert(END,song)
  
def playMusic():
    music_name = playlist.get(ACTIVE)
    mixer.music.load(playlist.get(ACTIVE))     
    mixer.music.play()   
    music.config(text = music_name[0:-4])

#Icon
logoIcon = PhotoImage(file="logo_icon.png")
root.iconphoto(False, logoIcon)

#Logo
logo = Image.open("logo_icon.png")
resized = logo.resize((180,180))
mainLogo = ImageTk.PhotoImage(resized)
Label(root, image=mainLogo, bg= "#191414").place(x=85,y=25)

#Buttons

#Play
play = Image.open("buttons/play.png")
resized = play.resize((50,50))
play = ImageTk.PhotoImage(resized)
Button(root, image=play, bg= "#191414", bd=0, command=playMusic).place(x=115,y=560)

#Pause
pause = Image.open("buttons/pause.png")
resized = pause.resize((50,50))
pause = ImageTk.PhotoImage(resized)
Button(root, image=pause, bg= "#191414", bd=0, command = mixer.music.pause).place(x=180,y=560)

#Resume
resume = Image.open("buttons/resume.png")
resized = resume.resize((50,50))
resume = ImageTk.PhotoImage(resized)
Button(root, image=resume, bg= "#191414", bd=0, command = mixer.music.unpause).place(x=50,y=560)

