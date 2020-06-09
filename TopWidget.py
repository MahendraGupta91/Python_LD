from tkinter import *

WELCOME_DURATION=10000
root = Tk()
root.iconbitmap("Dict_Icon.ico") 
root.columnconfigure(0, weight=1)
root.geometry("200x300") 
root.title("main") 

l = Label(root, text = "This is root window",bg="red") 
l.grid(row=0, column=0, sticky='ew', columnspan=1)

top = Toplevel() 
top.geometry("180x100") 
top.columnconfigure(0, weight=1)
top.title("toplevel")
top.configure(bg="#F8F8FF") 
l2 =Label(top, text = "Word", font="20", bg="#D2691E",fg="white")
#l2.grid(row=0, column=0, sticky="ew", columnspan=1)
#l3 =Label(top, text = "This is toplevel window")
m=Message(top, text="Message sdfgsdfg adfdfg sdfgsdfg dfsdfgsdfg ssdfg asdfsdf adfasdfasf adfadfasdf sdfsdfasf...", font="20")
#m.grid(row=1,column=0, sticky='ew')

l.pack() 
l2.pack()
#l3.pack()
m.pack()
#text.pack()
#top.after(WELCOME_DURATION, top.destroy) 

top.mainloop() 
