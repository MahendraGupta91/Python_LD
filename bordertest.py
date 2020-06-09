from tkinter import *

root = Tk()

def printt(self):
     repair = Tk()
     repairwindow = Frame(repair, bg='white', width=800, height=800)
     repairwindow.pack(expand=True, fill='both', side='right')
     repair.mainloop()


mainarea = Frame(root, bg='grey', width=1200, height=1000)
mainarea.pack(expand=True, fill='both', side='right')

label1 = Label( mainarea, width=40, height = 5 , text="New Quotation", 
relief=GROOVE )
label1.place(relx=.5, rely=.5, anchor="center")
label1.bind("<Button-1>",printt)

label2 = Label( mainarea, width=15, height = 3 , text="Update", 
relief=GROOVE 
)
label2.place(relx=.45, rely=.6, anchor="center")
label2.bind("<Button-1>",printt)

label3 = Label( mainarea, width=15, height = 3 , text="Report", 
relief=GROOVE )
label3.place(relx=.55, rely=.6, anchor="center")
label3.bind("<Button-1>",printt)

label4 = Label( mainarea, width=40, height = 5 , text="Data Base", 
relief=GROOVE )
label4.place(relx=.5, rely=.7, anchor="center")
label4.bind("<Button-1>",printt)

root.attributes('-alpha', 0.98)
root.mainloop()