from tkinter import *  
root = Tk()  
top=tkinter.Toplevel()
top.title("Toplevel Window")
for fm in ['blue','red','yellow','green','white','black']:  
    Frame(top,height = 20,width = 640,bg = fm).pack()  


root.mainloop()