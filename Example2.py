import tkinter as tk


root = tk.Tk()

def create_top():
    win = tk.Toplevel(root)
    #for fm in ['blue','red','yellow','green','black']:  
    f1=Frame(win,height = 20,width = 640,bg ='red')
    l1=Label(f1,text="Mahendra", fg="black")
    f1.pack()
    l1.pack()
        #Frame(win,height=20,width = 640,bg='white').pack()
        #f1.configure(bg="red")
#    f1.grid(row=0, column=0)
#    f2 =Frame(win,bg='green')
#    f2.grid(row=1, column=1)
#    tk.Label(f1, text="FRAME 1").grid()
#    tk.Label(f2, text="FRAME 2").grid()

tk.Button(root, text="ABC", command=create_top).grid(column=0, row=0)
tk.Label(root, text="FOO").grid(column=1, row=1)

root.mainloop()