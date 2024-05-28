"""
    https://www.tutorialspoint.com/how-can-i-use-tkinter-to-visualize-time-series-data
"""

import pymongo

from tkinter import *
#from tkinter import messagebox
import tkinter as tk
from dataclasses import dataclass

import random

window = tk.Tk()
# specify size of window.
window.geometry("720x500")

# Step 5: Enhancing the Visualization
x_label = tk.Label(window, text="Time")
x_label.pack()

y_label = tk.Label(window, text="Value")
y_label.pack()

# Create text widget and specify size.
#T = Text(window, height = 18, width = 80)
#T.pack()
canvas_width = 800
canvas_height = 200
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Create label for Date
#labeldate = Label(window, text = "Date shown here")
labeldate= Label(window, anchor= tk.SW, bg= "yellow", fg="black", text= "Date: "+ "will be here")
labeldate.config(font =("Courier", 18))
labeldate.pack()

# Create label to Temperature
label_T = Label(window, anchor= tk.SW, bg= "blue", fg="white", text= "Temperture: "+ "will be here")
label_T.config(font =("Courier", 18))
label_T.pack()  
      
# Create label to Humidity
label_H = Label(window, anchor= tk.SW, bg= "green", fg="white", text= "Humidity: "+ " will be here")
label_H.config(font =("Courier", 18))
label_H.pack()

#Visusalize
#Testdata = []
Tempdata = []
Humiddata = []

MONGODB_SERVER = "192.168.0.223" #Dell

myclient = pymongo.MongoClient("mongodb://"+MONGODB_SERVER+":27017/")
MYDB = myclient["Koti"]
MYCOL = MYDB["Parveke"]

myquery = { "Sensor": " SHT3X" }
myquery = { "Location": "Koti/Parveke" }

@dataclass
class Data:
    """Class for keeping track of an data to get from mongodb"""
    Currtemp  = 0
    CurrHumid = 0
    CurrDate = "none"


def mongodb_query():
    #mydocs = MYCOL.find(myquery).limit(10)
    #print("mongodb_query()")
    Tempdata.clear() 
    Humiddata.clear()
    #mydocs = MYCOL.find().limit(20).sort({"date" :-1}); 
    mydocs = MYCOL.find().sort({"Date" :-1}); 
     
    for doc in mydocs:
        #print(doc)
        #temp ="none"
        #humid="none"
        Data.CurrDate= doc["Date"]
        if "Temperature" in doc:
            Data.Currtemp = doc["Temperature"]
        if "Humidity" in doc:    
            Data.CurrHumid = doc["Humidity"]

        if"NodeInfo" in doc:
            pass  
            #print("Skip")
        else:
            if (Data.Currtemp != 0):
                Tempdata.append((Data.CurrDate, Data.Currtemp))
                #print(Data.CurrDate+ " Temp : "+str(Data.Currtemp)+ "°C")
            if (Data.CurrHumid != 0):
                Humiddata.append((Data.CurrDate, Data.CurrHumid)) 
                #print(Data.CurrDate+ " Humid: "+str(Data.CurrHumid)+"%")
 
    #print("Tempdata : "+str(Tempdata))
    #print("Humiddata: "+str(Humiddata))
    Data.Currtemp  = str(Tempdata[0][1])
    Data.CurrHumid = str(Humiddata[0][1])
    Data.CurrDate  = str(Tempdata[0][0])
    print("Date    : " + str(Data.CurrDate))
    print("TempNow : " + str(Data.Currtemp))
    print("HumidNow: " + str(Data.CurrHumid))

    window.title(doc["Location"])
     
# EOF #def monodb_query()
    
#Plotting the Time-Series Data
def plot_data():
   canvas.delete("all")
   x_scale = canvas_width / len(Tempdata)
   y_scale = canvas_height / 100

   for i in range(len(Tempdata) - 1):
      x1 = i * x_scale
      y1 = canvas_height - int(float(Tempdata[i][1])) * y_scale
      x2 = (i + 1) * x_scale
      y2 = canvas_height - int(float(Tempdata[i + 1][1])) * y_scale
      canvas.create_line(x1, y1, x2, y2, fill="blue", width=2)

   for i in range(len(Humiddata) - 1):
      x1 = i * x_scale
      y1 = canvas_height - int(float(Humiddata[i][1])) * y_scale
      x2 = (i + 1) * x_scale
      y2 = canvas_height - int(float(Humiddata[i + 1][1])) * y_scale
      canvas.create_line(x1, y1, x2, y2, fill="green", width=2)

      # Create label to Temperature
      #label_T = Label(window, anchor= tk.SW, bg= "blue", fg="white", text= "Temperture: "+ str(Data.Currtemp))
      #label_T.config(font =("Courier", 18))
      # Update Date label
      global labeldate
      labeldate["text"]= str(Data.CurrDate)
      labeldate.pack()
      # Update Temperature label
      global label_T
      label_T["text"]= "Temperture: "+ str(Data.Currtemp)
      label_T.pack()
      
      
      #label_H = Label(window, anchor= tk.SW, bg= "green", fg="white", text= "Humidity: "+ str(Data.CurrHumid))
      #label_H.config(font =("Courier", 18))
      # Create label to Humidity
      global label_H
      label_H["text"]= "Humidity: "+ str(Data.CurrHumid)
      label_H.pack()

# Scrollbar
#s = tNErollbar(windhow)
#s.pack(side=tk.RIGHT, fill=tk.Y)
#s.config(command=T.yview)

#T.config(yscrollcommand=s.set)

def query_and_plot():
    mongodb_query()
    plot_data()

def updateData():
   # pass
   query_and_plot()

def clear():
    canvas.delete("all")
   # T.delete("1.0", "end")
    
# Create button for next text.
b1 = Button(window, text = "Clear", 
            command = clear)
 
# Create an Exit button.
b2 = Button(window, text = "Exit",
            command = window.destroy) 

# Create an Clear button.
b3 = Button(window, text = "Update data",
            command = updateData)

b1.pack()
b2.pack()
b3.pack()

def main():
    #mongodb_query()
    #canvas.delete("all")
    #plot_data()
    query_and_plot()
    tk.mainloop()

if __name__ == '__main__':
    main()   