#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    v0.1   5'24   Yasperzee   Subscribe some MQTT Topics and send to MongoDb
    v0,2   5'24   Yasprrzee   Add dataclass    
"""
import paho.mqtt.client as paho
import pytz,json
import bson
from datetime import datetime 
from pymongo import MongoClient

from dataclasses import dataclass

TZHKI = pytz.timezone('Europe/Helsinki')

@dataclass
class Data:
    """Class for keeping track of an data to send to mongodb"""
    mongo_db = str      = "Test"    # location e.g Koti
    mongodb_collection  = str = "Testroom" # room e.g Keittio, Olohuone...

    MQTT_BROKER     = "192.168.0.152" #Rpi
    MONGODB_SERVER  = "192.168.0.223" #Dell

     # a tuple of (topic, qos)
    MQTT_TOPICS = [ ("Koti/Olohuone/NodeInfo",0),
                    ("Koti/Olohuone/Temperature",0),
                    ("Koti/Olohuone/Humidity",0),
                    ("Koti/Olohuone/Barometer",0),
                    ("Koti/Olohuone/Vcc",0),
                    ("Koti/Olohuone/Altitude",0),
                    ("Koti/Parveke/NodeInfo",0),
                    ("Koti/Parveke/Temperature",0),
                    ("Koti/Parveke/Humidity",0)                              
                  ]
    
    meas_float  = float = 0.0 
    nodemodel   = str = ""
    nodeid      = str = ""
    sensor      = str = ""

    #def total_cost(self) -> float:
     #   return self.unit_price * self.quantity_on_hand

data = Data

myclient = MongoClient("mongodb://"+data.MONGODB_SERVER+":27017/")    
print("Connected to the MongoDB database: "+ data.MONGODB_SERVER)  

def on_message(mosq, obj, msg): 
    datetime_utc = datetime.now(TZHKI) 
    print ("%s %-20s %s" % (datetime_utc.strftime('%Y:%m:%d %H:%M:%S'),msg.topic, msg.payload))
    print ("topic  : "+ msg.topic)
    print ("payload: "+ str(msg.payload)) 

    topics = msg.topic.split('/')
    #print ("topics  : "+ str(topics))
    data.mongo_db  = str(topics[0]) # Set Database
    data.mongodb_collection  = str(topics[1]) # Swt collection
    #print ("database  : "+ str(data.mongo_db))
    #print ("collection  : "+ str(data.mongodb_collection))

    if (topics[2] == "NodeInfo"):
        msg_str = str(msg.payload).split(':')
        msg_str = str(msg_str[1]).split(',')
        data.nodemodel = msg_str[0]
        data.nodeid = msg_str[1]
        tmp = msg_str[2].split("\'")
        data.sensor = tmp[0]
        data.meas_float = 0.0
        print ("                    nodemodel:" +data.nodemodel+ ", nodeid:"+data.nodeid +", sensor:" +data.sensor)
    else:
        meas_str = str(msg.payload).split("'")
        data.meas_float = float((meas_str)[1])
        data.meas_float= ("{:.2f}".format(data.meas_float))
        #   print("data "+ data.meas_float)

    mydb  = myclient[str(data.mongo_db)]
    mycol = mydb[str(data.mongodb_collection)]
    
    #myresult = mycol.find().limit(1)
    #print the result:
    #for x in myresult:
    #    print(x)
    
    mycol.insert_one({	
        "Location": topics[0]+ "/" + topics[1],
        "NodeModel": data.nodemodel,   
        "NodeID": data.nodeid,
        "Sensor": data.sensor, 
        "Date": datetime_utc.strftime('%Y:%m:%d %H:%M:%S'),
        topics[2]: data.meas_float
    })

def main():
    client = paho.Client(paho.CallbackAPIVersion.VERSION2)
    client.on_message = on_message
    client.connect(data.MQTT_BROKER, 1883, 60)
    client.subscribe(data.MQTT_TOPICS) 

    while client.loop() == 0:
        pass

if __name__ == '__main__':
    main()     