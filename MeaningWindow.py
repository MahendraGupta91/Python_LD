import tkinter as tk

root = tk.Tk()


def create_top():
    win = tk.Toplevel(root)
    win.iconbitmap("BlackLogo.ico")
    win.rowconfigure(1, weight=1)
    win.columnconfigure(1, weight=1)
    win.title("Meaning")
    f1 = tk.Frame(win, height=30, bg='#1A5266')
    #f1.grid_propagate(0)
    f1.grid(row=0, column=0,sticky="nsew")
    f2 = tk.Frame(win,height=100,bg='#effbfe')
    f3 = tk.Frame(win,height=100,bg='#effbfe')
    #f2.grid_propagate(0)
    f2.grid(row=1, column=0,sticky="nsew")
    f3.grid(row=2, column=0,sticky="nsew")
    tk.Label(f1, text="FRAME1", bg='#1A5266', fg="white",font="Times 16 bold",anchor="e").grid()
    #tk.Label(f2, text="FRAME 2",fg="black",bg='#effbfe', width=20,font="Helvetica 16",anchor="e").grid()
    tk.Message(f2,text="Message to Lover. jljsdfs sdfsdf sdfsdfsdf sdfsfsdf",fg="black",bg='#effbfe',font="Times 14", anchor="e").grid()
    tk.Message(f3,text="Message to Lover. jljsdfs sdfsdf sdfsdfsdf sdfsfsdf kjhs khshd hhasdas khhlsad jhlsdl jljsd jljalsd jljasld ljljasd jlasjdj ",fg="black",bg='#effbfe',font="Times 14").grid()

tk.Button(root, text="ABC").grid(column=0, row=0)
tk.Label(root, text="FOO").grid(column=1, row=1)

root.after(10, create_top)
root.mainloop()