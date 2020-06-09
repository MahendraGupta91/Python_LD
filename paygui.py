import tkinter
from tkinter import Toplevel

WELCOME_MSG = '''Welcome to this event.

Your attendance has been registered.

Don't forget your free lunch.'''
WELCOME_DURATION = 2000

def welcome():
    top = Toplevel()
    top.title('Welcome')
    Message(top,text=WELCOME_MSG, padx=20, pady=20).pack()
    top.after(WELCOME_DURATION, top.destroy)
root =tkinter.Tk()
tkinter.Button(root, text="Click to register", command=welcome).pack()
root.mainloop()