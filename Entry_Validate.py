import tkinter as tk

def next_step():
    if mandatory_entry.get():
        # the user entered data in the mandatory entry: proceed to next step
        print("next step")
        root.destroy()
    else:
        # the mandatory field is empty
        print("mandatory data missing")
        mandatory_entry.focus_set()

root = tk.Tk()

mandatory_entry = tk.Entry(root)

tk.Label(root, text="Data *").grid(row=0, column=0)
mandatory_entry.grid(row=0, column=1)
tk.Button(root, text='Next', command=next_step).grid(row=1, columnspan=2)

root.mainloop()