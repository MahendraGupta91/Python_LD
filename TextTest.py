from tkinter import *

def callUpdater():
    text = textBox.get()
    textBox.delete(0, 'end')
    chat.configure(state='normal')
    chat.insert('end', text + '\n')
    chat.configure(state='disabled')

root = Tk()
chatBox = Scrollbar(root)
chat = Text(root, wrap='word', state='disabled', width=50,
            yscrollcommand=chatBox.set)
chatBox.configure(command=chat.yview)

chat.grid(row=0, columnspan=2, sticky='ewns')
chatBox.grid(row=0, column=2, sticky='ns')
Label(root, text="Input: ").grid(row=1, column=0)

textBox = Entry(root, bd=0, width=40, bg="pink")
textBox.grid(row=1, column=1)

Button(root, text="Send", command=callUpdater).grid(row=2, columnspan=2)
root.mainloop()