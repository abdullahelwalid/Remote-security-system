# Project description:
#[SSL project
# SSL (security system locker) this project is aimed to make a 
# DC motor connected to a rassberry pi rotate and get activated.
# For future purposes, the program will be connected to the internet 
# so that the motor will recieve data from any authorized user from 
# any part of the world  connected to the server]

#project status: 
#[On development phase
#Not yet completed 
#Waiting for hardware to be shipped]


import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

#window
window = tk.Tk()

frame = tk.Frame(window)
frame.pack()

#icon
window.iconbitmap("icon.ico")

#logo
img = ImageTk.PhotoImage(Image.open("logo.jpg"))
logo = tk.Label(image=img)
logo.pack()

#below logo
img1 = ImageTk.PhotoImage(Image.open("belowlogo.jpg"))
logo1 = tk.Label(image=img1)
logo1.place(x=145, y=300)

#window title
window.title("SECURITY SYSTEM")

#window size
window.geometry('500x500')

#window lable
name = tk.Label(window,
    text="Enter password",
    foreground="white",#text color
    background="black")

name.place(x=190, y=180)

#password Entry
entry = tk.Entry(window, show="*")
entry.place(x=150, y=200)

#not eligble
def eligble():
    label_1 = tk.Label(window, text="NOT ELIGBLE ", fg="red")
    label_1.place(x=200, y=250)

# Password
def prd():
    password = entry.get().upper()
    if password == "ABDULLAH" or password == "Walid" or password == "walid" or password == "Elwalid" or password == "elwalid":
        label_1 = tk.Label(text="WELCOME SIR ",fg="green")
        label_1.place(x=200, y=270)
        welcome()
    else:
        eligble()
        warning()
        warning_text()
        #window.quit()

# If password is correct
def welcome():
    import simpleaudio as sa
    filename = '[ONTIVA.COM]-Welyn Welcome back sound effect [Resub sound]-HQ.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    

# if password is wrong
def warning():
    import simpleaudio as sa
    filename = 'mixkit-alarm-clock-beep-988.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def warning_text():
    warning_text = messagebox.showinfo("ERROR", "Wrong Security Code")




#button
button = tk.Button(window,
    text="NEXT",
    foreground="blue",#text color
    background="white",
    command=prd)

button.place(x=220, y=230)
#loop
window.mainloop()



#person = str(input("write your name: "))



#if value in object:
#     print('wlc')
# #else:
#     print('get out man')