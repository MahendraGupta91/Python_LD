import tkinter
from tkinter import Toplevel

master = tkinter.Tk()
#
##master.configure(background='SteelBlue1')
#master.columnconfigure(0, weight=1) # make the column 1 expand when the window is resized
#nb_of_columns = 2 # to be replaced by the relevant number
#titlelabel =Label(master, text="my Title", fg="blue4", bg ="red")
#titlelabel.grid(row=0, column=0, sticky='ew', columnspan=1) # sticky='ew' expands the label horizontally


top = Toplevel()
top.geometry("180x100") 
m=tkinter.Message(top,text="Hello Toplevel").pack()
top.title("toplevel")
top.configure(bg="#F8F8FF") 
#l2 =Label(top, text = "Word", font="20", bg="#D2691E",fg="white",)
#l2.grid(row=0, column=0, sticky='ew', columnspan=1)
#l2.pack()
master.geometry('200x200')
master.mainloop()