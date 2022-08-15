############################################# IMPORTING ################################################
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import cv2,os
import csv
import numpy as np
from PIL import Image
import pandas as pd
import datetime
import time
from geopy.geocoders import Nominatim
#########################################################
def detect():
    

# capture frames from a video
    cap = cv2.VideoCapture(r"D:\accident.mp4")

# Trained XML classifiers describes some features of some object we want to detect
    vars_cascade = cv2.CascadeClassifier(r"C:\Users\LENOVO\OneDrive\Desktop\ROAD ACCIDENT DETECTION\Car-Detection-Basic-Open-CV-master\vech.xml")

# loop runs if capturing has been initialized.
    while True:
        ret, frames = cap.read()
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        vars = vars_cascade.detectMultiScale(gray, 1.4, 2)
        for (x, y, w, h) in vars:
            cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 0, 255), 2)
            print("ACCIDENT DETECTED")
         
        cv2.imshow('PBLGROUP', frames )
        if cv2.waitKey(33) == 27:
            break
# De-allocate any associated memory usage

cv2.destroyAllWindows()
   

############################################# FUNCTIONS ################################################

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

##################################################################################

def tick():
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    clock.after(200,tick)

###################################################################################

def contact():
    mess._show(title='Contact us', message="Please contact us on : 'adityasingh99048@gmail.com' ")

###################################################################################
def AMBULANCE():
    # calling the nominatim tool
    geoLoc = Nominatim(user_agent="GetLoc")
 
    # passing the coordinates
    locname = geoLoc.reverse("26.7674446, 81.109758")
 
    # printing the address/location name
    print(locname.address)

    
###################################################################################
# Designing window for registration
 
def register():
    global register_screen
    register_screen = tk.Toplevel()
    register_screen.title("Register")
    register_screen.geometry("720x360")
    register_screen.configure(background='white')

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="green",font=('times', 17, ' bold ')).pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ",fg="black",font=('times', 17, ' bold '))
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ",fg="black",font=('times', 17, ' bold '))
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="green",fg="black",font=('times', 17, ' bold '), command = register_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel()
    login_screen.title("Login")
    login_screen.configure(background='white')
    login_screen.geometry("720x360")
    Label(login_screen, text="LOGIN PAGE",bg="green", width=20  ,height=1  ,fg="white",font=('times', 17, ' bold ')).pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ",fg="black",font=('times', 17, ' bold ')).pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ",fg="black",font=('times', 17, ' bold ')).pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success Login to continue", fg="green", font=("times", 15,'bold')).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
##################################
'''class My_Button(Button):
    def __init__(self, text, row, col, command, color=None, **kwargs):
        self.text = text
        self.row = row
        self.column = col
        self.command = command
        self.color = color
        super().__init__()
        self['bg'] = self.color
        self['text'] = self.text
        self['command'] = self.command
        self.grid(row=self.row, column=self.column)
def dothings():
    print("All Fine")
    cars_cascade = cv2.CascadeClassifier('haarcascade_car.xml')

    def detect_cars(frame):
        cars = cars_cascade.detectMultiScale(frame, 1.15, 4)
        for (x, y, w, h) in cars:
            cv2.rectangle(frame, (x, y), (x+w,y+h), color=(0, 255, 0), thickness=2)
        return frame

    def Simulator():
        CarVideo = cv2.VideoCapture('testvideo.mp4')
        while CarVideo.isOpened():
            ret, frame = CarVideo.read()
            controlkey = cv2.waitKey(1)
            if ret:        
                cars_frame = detect_cars(frame)
                cv2.imshow('frame', cars_frame)
            else:
                break
            if controlkey == ord('q'):
                break

        CarVideo.release()
        cv2.destroyAllWindows()

    Simulator()'''
#####################
        
# Designing popup for login success
################################################
    #Button(register_screen, text="Register", width=10, height=1, bg="green",fg="black",font=('times', 17, ' bold '), command = register_user).pack()

    
#################################################
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("720x360")
    Label(login_success_screen, text="Login Success",width=20,height=1,font=('times', 17, ' bold ')).pack()
    Button(login_success_screen, text="DETECT",width=10,height=1,bg="green",fg="black",font=('times', 17, ' bold '),command=detect).pack()
    class My_Button(Button):
        def __init__(self, text, row, col, command, color, **kwargs):
            self.text = text
            self.row = row
            self.column = col
            self.command = command
            self.color = color
            super().__init__()
            self['bg'] = self.color
            self['text'] = self.text
            self['command'] = self.command
            self.grid(row=self.row, column=self.column)



##########################################################################################

def check_haarcascadefile():
    exists = os.path.isfile("haarcascade_frontalface_default.xml")
    if exists:
        pass
    else:
        mess._show(title='Some file missing', message='Please contact us for help')
        window.destroy()

###################################################################################
    
global key
key = ''

ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
day,month,year=date.split("-")

mont={'01':'January',
      '02':'February',
      '03':'March',
      '04':'April',
      '05':'May',
      '06':'June',
      '07':'July',
      '08':'August',
      '09':'September',
      '10':'October',
      '11':'November',
      '12':'December'
      }
######################################## GUI FRONT-END #######################################

window=tk.Tk()
window.geometry("1280x720")
window.resizable(True,False)
window.title("ROAD ACCIDENT DETECTION SYSTEM")
window.configure(background='white')

frame1 = tk.Frame(window, bg="#ADD8E6")
frame1.place(relx=0.11, rely=0.17, relwidth=0.39, relheight=0.80)

frame2 = tk.Frame(window, bg="#ADD8E6")
frame2.place(relx=0.51, rely=0.17, relwidth=0.38, relheight=0.80)

message3 = tk.Label(window, text="ROAD ACCIDENT DETECTION SYSTEM" ,fg="#66FCF1",bg="#1F2833" ,width=55 ,height=1,font=('times', 29, ' bold '))
message3.place(x=10, y=10)

frame3 = tk.Frame(window, bg="#0000FF")
frame3.place(relx=0.52, rely=0.09, relwidth=0.09, relheight=0.07)

frame4 = tk.Frame(window, bg="#000000")      
frame4.place(relx=0.36, rely=0.09, relwidth=0.16, relheight=0.07)

datef = tk.Label(frame4, text = day+"-"+mont[month]+"-"+year+"  |  ", fg="orange",bg="#262523" ,width=55 ,height=1,font=('times', 22, ' bold '))
datef.pack(fill='both',expand=1)

clock = tk.Label(frame3,fg="orange",bg="#262523" ,width=55 ,height=1,font=('times', 22, ' bold '))
clock.pack(fill='both',expand=1)
tick()
lbl = tk.Label(frame2, text="REGISTRATION/LOGIN",width=20  ,height=1  ,fg="white"  ,bg="black" ,font=('times', 17, ' bold ') )
lbl.place(x=80, y=55)
lbl = tk.Label(frame1, text="PROJECT NAME",width=20  ,height=1  ,fg="white"  ,bg="black" ,font=('times', 17, ' bold ') )
lbl.place(x=80, y=55)
lbl = tk.Label(frame1, text="सड़क परिवहन",width=20  ,height=1  ,fg="white"  ,bg="black" ,font=('times', 20, ' bold ') )
lbl.place(x=80, y=145)
####################################
menubar = tk.Menu(window,relief='ridge')
filemenu = tk.Menu(menubar,tearoff=0)
filemenu.add_command(label='Contact Us', command = contact)
filemenu.add_command(label='GET THE LOCATION', command = AMBULANCE)
filemenu.add_command(label='Exit',command = window.destroy)
menubar.add_cascade(label='Help',font=('times', 29, ' bold '),menu=filemenu)
###############################
"""detect = tk.Button(frame2, text="DETECT", command=detect  ,fg="white"  ,bg="#7C1034"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
detect.place(x=30, y=300)"""
register = tk.Button(frame2, text="REGISTER", command=register  ,fg="white"  ,bg="#7C1034"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
register.place(x=30, y=300)
login = tk.Button(frame2, text="LOGIN", command=login  ,fg="white"  ,bg="#7C1034"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
login.place(x=30, y=220)


quitWindow = tk.Button(frame1, text="Quit", command=window.destroy  ,fg="white"  ,bg="#7C1034"  ,width=35 ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
quitWindow.place(x=30, y=220)
contact = tk.Button(frame1, text="CONTACT US", command=contact  ,fg="white"  ,bg="#7C1034"  ,width=35 ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
contact.place(x=30, y=300)


##################### END ######################################

window.configure(menu=menubar)
window.mainloop()


