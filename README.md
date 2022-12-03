# Music Player
--------------

## Introduction

Various music player apps have been created as a result of technological advancements. 
These apps offer a wide range of features and functionalities. 
Some apps, however, charge a monthly subscription fee to remove advertisements.
But Python makes it possible for us to create a functional music player for free.
So, in this project, we'll utilize its tools to build an MP3 player.

## How to Setup
We must first get all the prerequisites ready in order for this project to succeed.

  * Install ***Python 3.11.0*** for **pip**,  **tcl/tk**, and **IDLE** <br />
  * Copy the installation directory. e.g. `C:\Python\Python311` <br />
  * Add the directory in ***PATH*** environent variable. <br />

### Installing Libraries

Check to see if Python and a code editor are both installed on your computer. <br />
To determine whether Python is installed, use the command listed below.  <br />
`python --version` <br />
Regardless of the OS you are using, this command will function.

The pygame library needs to be installed as well. To execute the installation command, we'll use PIP. <br />
`pip install pygame` <br />

By using the command below, Pillow library is used for resizing the image input to the program. <br />
`pip install Pillow` <br />






### Importing Modules 

The modules that we have installed must be imported before we can utilize them,
specifically a few packages that are compatible with our project.
The following code will allow us to utilize the modules. <br />

#importing libraries <br />
**import os <br />
from tkinter import * <br />
from tkinter import Tk <br />
from tkinter import filedialog <br />
from pygame import mixer <br />
from PIL import ImageTk, Image** <br />


### Creating Root Window
Our application's layout, containing all necessary components, will be in the root window. 
You can set the window's title and dimensions using the code below.

**root=Tk() <br />
root.title('ACP Music Player') <br />
root.geometry("920x670+290+85") <br />
root.configure(bg= "#0f1a2b") <br />
root.resizable(False, False) <br />
mixer.init()** <br />



  
