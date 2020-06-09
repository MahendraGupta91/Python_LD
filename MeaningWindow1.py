import tkinter as tk

root = tk.Tk()
root.iconbitmap("BlackLogo.ico")
root.title("LearnDifferences.org")
root.configure(bg='#1A5266')


Eng_meaning="Mahendra"
Hindi_meaning="Gupta"
#action_with_arg=meaning_window(Eng_meaning,Hindi_meaning)

def meaning_window():
    win = tk.Toplevel(root)
    win.iconbitmap("BlackLogo.ico")
    win.rowconfigure(1, weight=1)
    win.columnconfigure(1, weight=1)
    win.title("Meaning")
    f1 = tk.Frame(win, height=30, bg='#1A5266')
    #f1.grid_propagate(0)
    f1.grid(row=0, column=0,sticky="nsew")
    f0=tk.Frame(win,bg="#effbfe")
    f0.grid(row=1, column=0,sticky="nsew")
    
    f2 = tk.Frame(f0,height=100,bg='#effbfe')
    f3 = tk.Frame(f0,height=100,bg='#effbfe')
    f4 = tk.Frame(f0,height=100,bg='#effbfe')
    f5 = tk.Frame(f0,height=100,bg='#effbfe')
                  
    #f2.grid_propagate(0)
    f2.grid(row=0, column=0,sticky="nsew")
    f3.grid(row=0, column=1,sticky="nsew")
    f4.grid(row=1, column=0,sticky="nsew")
    f5.grid(row=1, column=1,sticky="nsew")
    tk.Label(f1, text="FRAME1", bg='#1A5266', fg="white",font="Times 16 bold",anchor="e").grid()
    #tk.Label(f2, text="FRAME 2",fg="black",bg='#effbfe', width=20,font="Helvetica 16",anchor="e").grid()
    tk.Message(f2,text="E:",fg="black",bg='#effbfe',font="Times 14", anchor="e").grid()
    tk.Message(f3,text=Eng_meaning,fg="black",bg='#effbfe',font="Times 14").grid()
    tk.Message(f4,text="H:",fg="black",bg='#effbfe',font="Times 14", anchor="e").grid()
    tk.Message(f5,text=Hindi_meaning,fg="black",bg='#effbfe',font="Times 14").grid()

hi=tk.Frame(root,height=10,width=200,bg='#1A5266').grid(column=0,row=0)
#tk.Label(hi,text="FRAME1ffffffff", bg='#1A5266', fg="white",font="Times 16 bold", LEFT).grid()
#tk.Label(hi,text="Type the word:", bg='white',fg="white").grid()
tk.Entry(root, text="ABC").grid(column=0, row=1)
tk.Frame(root,height=5,width=200,bg='#1A5266').grid(column=0,row=2)
tk.Button(root, text="submit",command=meaning_window).grid(column=0, row=3)
tk.Frame(root,height=20,width=200,bg='#1A5266').grid(column=0,row=4)
tk.Button(root, text="Clipboard",command=meaning_window).grid(column=0, row=5)
inst=tk.Frame(root,height=2,width=200,bg='#1A5266').grid(column=0,row=6)
tk.Label(inst,text="To get meaning, type and press submit \n or copy the word and press clipboard",fg="white",bg='#1A5266').grid()

#root.after(10, meaning_window)
root.mainloop()