import tkinter as tk

root = tk.Tk()

def create_top():
    win = tk.Toplevel(root)
    f1 = tk.Frame(win)
    f1.grid(row=0, column=0)
    f2 = tk.Frame(win)
    f2.grid(row=1, column=1)
    tk.Label(f1, text="FRAME 1").grid()
    tk.Label(f2, text="FRAME 2").grid()

tk.Button(root, text="ABC").grid(column=0, row=0)
tk.Label(root, text="FOO").grid(column=1, row=1)

root.after(10, create_top)
root.mainloop()