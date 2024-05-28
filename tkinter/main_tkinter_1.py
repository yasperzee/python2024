
#rom tkinter.simpledialog import askinteger
#from tkinter import *
#from tkinter import messagebox


import tkinter as tk
window = tk.Tk()
text_box = tk.Text()
text_box.pack()


# Create an event handler
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    #print(event.char)
    text_box.insert("1.0", "TERSE")
text_box.insert("2.5", "\nMoro nääs")

window.mainloop()
