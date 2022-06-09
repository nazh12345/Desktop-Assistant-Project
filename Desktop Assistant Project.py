import speech_recognition as sr
import tkinter as tk
from tkinter import *
from tkinter.ttk import *

import pyttsx3
import os
import webbrowser
friend=pyttsx3.init()
listener = sr.Recognizer()

def speaktext(text):
    friend.say(text)
    friend.runAndWait()

def greetings():                                    # function to wish the user according to the daytime
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk('Good Morning')

    elif hour>12 and hour<18:
        talk('Good Afternoon')

    else:
        talk('Good Evening')

    talk('Hello I am your Desktop Assistant, your Artificial intelligence assistant. Please tell me how may I help you')


def getaudio():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def bot():
    while True:
        query= getaudio()
        print(query)
        if "hello" in query:
            speaktext("hello")
        elif "calculator" in query:
            speaktext('Opening calculator now')
            webbrowser.open('calculator:')
        elif "open google" in query:
            speaktext("Google Chrome")
            webbrowser.open("google.com")
        elif "open youtube" in query:
            speaktext("Opening Youtube now")
            webbrowser.open("youtube.com")
        elif "open youtube" in query:
            speaktext("Opening youtube now")
            webbrowser.open("youtube.com")
        elif 'open gmail' in query:
            speaktext("Opening gmail now")
            webbrowser.open("mail.google.com")
        elif 'open camera' in query:
            speaktext("Opening camera now")
            webbrowser.open("microsoft.windows.camera:")
        elif 'how are you' in query:
            speaktext("I am fine, Thank you for asking. I hope you are doing well too!")

        else:
            speaktext('please speak again')
           
def message_bx():
    top = Toplevel()
    top.geometry("600x45")
    top["bg"] = "#99FFCC"
    text1="""1) To give in command please click on the mic button
             2) To open Google, YouTube, Camera, Email and Calculator please say "Open 'app name' 
    """
    current_label1 = Label(top, text=text1,
    justify='center', width=200)
    current_label1.pack()
    top.mainloop()
# creating tkinter window
root = Tk()
root["bg"] = "#99FFCC"

# Adding widgets to the root window
Label(root, text = 'Desktop Assistant', font =(
'Verdana', 15)).pack(side = TOP, pady = 10)

# Creating a photoimage object to use image
photo = PhotoImage(file ="C:/Users/PC-1/Downloads/mic-removebg-preview.png")

# here, image option is used to
# set image on button
Button(root, text = 'Click Me !',command=bot, image = photo ).pack(side = RIGHT)
Button(root, text = 'Help',command=message_bx).pack(side = BOTTOM)


mainloop()

