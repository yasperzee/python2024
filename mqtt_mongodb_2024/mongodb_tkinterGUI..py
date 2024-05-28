
import pymongo

from tkinter import *
#from tkinter import messagebox
import tkinter as tk
window = tk.Tk()

# specify size of window.
window.geometry("600x450")

# Create text widget and specify size.
T = Text(window, height = 18, width = 80)

MONGODB_SERVER = "192.168.0.223" #Dell

myclient = pymongo.MongoClient("mongodb://"+MONGODB_SERVER+":27017/")
MYDB = myclient["home_iot"]
MYCOL = MYDB["koti"]

myquery = { "Sensor": "SHT-31" }

z=""
a=""

mydocs = MYCOL.find(myquery).limit(25)
for doc in mydocs:
    #print(doc)
    y = doc["date"]
    if "Temperature" in doc:
        z = doc["Temperature"]
    if "Humidity" in doc:    
        a = doc["Humidity"]
    row = (y+ "  Temp: "+str(z)+ "C  Humid: "+str(a)+"%\n")
    print(row)
    T.insert(tk.END, row)



# Create label
l = Label(window, text = "Measurements from MongoDb")
l.config(font =("Courier", 14))

# Scrollbar
s = tk.Scrollbar(window)
s.pack(side=tk.RIGHT, fill=tk.Y)
s.config(command=T.yview)

T.config(yscrollcommand=s.set)

Fact = "A man can be arrested in Italy for wearing a skirt in public."
 
def addText():
    T.insert(tk.END, "Button3 pushed!\n")

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
#T.insert(tk.END, row)
#T.insert(tk.END, "\nTESTING!!")

tk.mainloop()

