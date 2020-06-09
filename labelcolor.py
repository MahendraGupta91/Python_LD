import tkinter
import Toplevel

master = tkinter.Tk()

master.configure(background='SteelBlue1')
master.columnconfigure(1, weight=1)

nb_of_columns = 2 # to be replaced by the relevant number
titleframe = tkinter.Frame(master, bg ="gray80")
titleframe.grid(row=0, column=0, columnspan=nb_of_columns, sticky='ew')
titlelabel = tkinter.Label(titleframe, text="my Title", fg="blue4", bg ="gray80")
titlelabel.grid(row=0, column=1)

top=Toplevel()
top.title("Toplevel Window")

# other widgets on the same row:
#tkinter.Button(titleframe, text='Ok').grid(row=0, column=3)

master.geometry('200x200')
master.mainloop()