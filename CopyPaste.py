import tkinter
from tkinter import messagebox
import pyperclip
window=tkinter.Tk();
window.title("Meaning Helper")
LabelText=tkinter.StringVar()
  
label=tkinter.Label(window, textvariable=LabelText, font=("Arial Bold",15)).pack();
#LabelText.set("Message will Be shown here")
#bt=tkinter.Button(window, text="Show", bg="blue", font=("Arial Bold", 20)).pack();
def clicked():
    #print(LabelText.)
    messagebox.showinfo("Hello Python", "Hello World");
    messagebox.showinfo()
    messagebox.showwarning()
    messagebox.showerror()
    messagebox.askquestion()
    messagebox.askokcancel()
    messagebox.askyesno()
    messagebox.askretrycancel()
    LabelText.set(pyperclip.paste())
    #label.configure(text=pyperclip.paste())
bt=tkinter.Button(window, text="Show", command=clicked)
bt.pack()
#print(pyperclip.paste())
window.geometry("350x200")
window.mainloop();

