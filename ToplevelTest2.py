import tkinter
from tkinter import Toplevel

WELCOME_MSG = '''Welcome \n to this event.\nYour attendance has been registered.
Don't forget your free lunch.'''
WELCOME_DURATION = 4000

def welcome():
    top = tkinter.Tk()
    top.title('Welcome')
    #top.config(bg="red")
    #tkinter.Message(top,text=WELCOME_MSG, padx=20, pady=20,bg="green", font="20").pack()
    #print(s)
    top.after(WELCOME_DURATION, top.destroy)
root =tkinter.Tk()
tkinter.Button(root, text="Click to register", command=welcome).pack()
root.mainloop()