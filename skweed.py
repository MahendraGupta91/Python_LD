from tkinter import *

root = Tk()
#root.rowconfigure(1, weight=1)
#root.columnconfigure(1, weight=1)

leftFrame = Frame(root, width = 200, height = 200, bg = 'green')
leftFrame.grid(row = 0, column = 0, sticky="nesw")

centerFrame = Frame(root, width = 200, height = 200, bg = 'black')
centerFrame.grid(row = 1, column = 1)

rightFrame = Frame(root, width = 200, height = 200, bg = 'blue')
rightFrame.grid(row = 2, column = 2) 

b = Label(leftFrame, text = "Press me!", bg = 'green')
#b.grid()
root.mainloop()