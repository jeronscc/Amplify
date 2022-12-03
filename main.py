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
