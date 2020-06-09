from Tkinter import*
def quit():
    print('Hello, getting out of here')
import sys; sys.exit()
root=Tk();
widget=Button(root, text='Press me to quit' , command=quit)
widget.pack()
widget.mainloop()