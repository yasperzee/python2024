
#rom tkinter.simpledialog import askinteger
from tkinter import *
#from tkinter import messagebox
import tkinter as tk
window = tk.Tk()

# specify size of window.
window.geometry("250x200")

# Create text widget and specify size.
T = Text(window, height = 20, width = 80)

# Create label
l = Label(window, text = "Fact of the Day")
l.config(font =("Courier", 14))

Fact = "A man can be arrested in Italy for wearing a skirt in public."
 
def addText():
    T.insert(tk.END, "\nButton3 pushed!")

def clearText():
    T.delete("1.0", "end")
    
# Create button for next text.
b1 = Button(window, text = "Clear", 
            command = clearText)
 
# Create an Exit button.
b2 = Button(window, text = "Exit",
            command = window.destroy) 

# Create an Clear button.
b3 = Button(window, text = "AddText",
            command = addText)

l.pack()
T.pack()
b1.pack()
b2.pack()
b3.pack()
 
# Insert The Fact.
T.insert(tk.END, Fact)
T.insert(tk.END, "\nTESTING!!")

tk.mainloop()

