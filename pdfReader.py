from tkinter import *
from tkdocviewer import *

# Create a root window
root = Tk()

# Create a DocViewer widget
v =DocViewer(root)
v.pack(side="top", expand=1, fill="both")

# Display some document
v.display_file("DataSampling.pdf")

# Start Tk's event loop
root.mainloop()