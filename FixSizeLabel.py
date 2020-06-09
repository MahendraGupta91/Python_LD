import tkinter as tk
import json
root = tk.Tk()
root.geometry("500x300")
oldWords={"mahi":"Mahendra"}
i=0

def update_text_dictionary():
    with open('FixedSize.json', 'w') as dict_writer:
        json.dump(oldWords, dict_writer)
        print("updated")
        root.destroy()

def add():
    global i
    i=i+1
    oldWords[i]="Mahendra"
    tk.Entry(frame).grid()

def disable():
    frame.configure(height=frame["height"],width=frame["width"])
    frame.grid_propagate(0)

def enable():
    frame.grid_propagate(1)

frame = tk.Frame(root, height=100,width=150,bg="black")
frame.grid(row=1,column=0)

tk.Button(root, text="add widget", command=add).grid(row=0,column=0)
tk.Button(root, text="disable propagation", command=disable).grid(row=0,column=1)
tk.Button(root, text="enable propagation", command=enable).grid(row=0,column=2)
root.protocol("WM_DELETE_WINDOW",update_text_dictionary)
root.mainloop()