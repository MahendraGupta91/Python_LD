import tkinter as tk

root = tk.Tk()


def create_top():
    win = tk.Toplevel(root)
    win.rowconfigure(1, weight=1)
    win.columnconfigure(1, weight=1)
    win.title("Toplevel")
    f1 = tk.Frame(win, height=50, width=400, bg='red')
    f1.grid_propagate(0)
    f1.grid(row=0, column=0,sticky="nsew")
    f2 = tk.Frame(win,height=20, width=400,bg='black')
    f2.grid(row=1, column=0,sticky="nsew")
    tk.Label(f1, text="FRAME1", bg='red',width=20,font=20,anchor="e").grid()
    tk.Label(f2, text="FRAME 2").grid()

tk.Button(root, text="ABC").grid(column=0, row=0)
tk.Label(root, text="FOO").grid(column=1, row=1)

root.after(10, create_top)
root.mainloop()