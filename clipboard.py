from tkinter import*
def quit():
    print('Hello, getting out of here')
root=Tk()
Button(root, text='Press me to quit' , command=quit)
Button (root, text='Press Me', command=root.quit).pack(side=LEFT)
#print (" "+clipboard_append('i can has clipboardz?'))
root.mainloop()