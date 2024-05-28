#!/usr/bin/ python

# ***************** python3 paho_mqtt_client.py ********************************
#
#   Description:    Subscribe selected sensors to mqtt run_local_server
#                   and send values to local databse
#
#   Sensors:        BMP-180 / BMP-280 (temperature, pressure)
#                   BME-280 (temperature, pressure, humidity)
#                   DTH-11 / DTH22 (temperature,humidity)
#                   TEMT6000 (AmbientLight)
#
#   Dependencies:   Install paho-mqtt for python3 with pip3
#                   To obtain the full code, including examples and tests,
#                   you can clone the git repository:
#                       git clone https://github.com/eclipse/paho.mqtt.python
#
#*******************************************************************************

"""------- Version history -----------------------------------------------------
    v0.1    yasperzee   5'24   Created

#TODO:
-----------------------------------------------------------------------------"""

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import tkinter as tk
#import json
import random
import time

from configuration import MQTT_PORT, MQTT_KEEPALIVE, MQTT_CLIENT_ID, MQTT_RECONN_DELAY
from MqttNodeHandler import ReadMqttData
from MqttNodeHandler import on_connect
from MqttNodeHandler import on_disconnect
from MqttNodeHandler import on_message

from mqtt_conf import MQTT_HOST

mqtt_data_handler = ReadMqttData()

window = tk.Tk()
frame = tk.Frame(master=window, width=150, height=150)
frame.pack()
text1 =" This is text1"
text2 =" This is text2"

location ="Koti"
room ="Olohuone"
sensor = "Ilmanpaine:   "
value = 97

msgs = [{'topic': "kids/yolo", 'payload': "jump"},
        {'topic': "adult/news", 'payload': "extra extra"},
        {'topic': "adult/news", 'payload': "super extra"}]

def main():

   # Set mqtt client and callbacks
    # mqtt_client = mqtt.Client(MQTT_CLIENT_ID)
    mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    mqtt_client.loop_start()
    mqtt_client.on_connect = on_connect
    mqtt_client.on_disconnect = on_disconnect

    mqtt_client.on_message = on_message
    # reconnect_delay_set(min_delay=1, max_delay=120)
    connected = False

    try:
       mqtt_client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE)
       # mqtt_client.connect(MQTT_HOST, MQTT_PORT)
    except IOError as e:
        connected = False
        if e.errno == 101:
            print ("Network Error")
            #time.sleep(1)
    else:
        print("Mqtt server connected " + MQTT_HOST)
        connected = True
    finally:
        if not connected:
            print("Mqtt server reconnecting: " + MQTT_HOST)
            mqtt_client.reconnect_delay_set(MQTT_RECONN_DELAY)
            try:
                mqtt_client.reconnect();
            except IOError as e:
                connected = False
                if e.errno == 101:
                    print ("Network Error")          
            else:
                print("Mqtt server connected " + MQTT_HOST)

        #while True:

        mqtt_client.loop_start()
        i=0

        

        while (i<10):
            time.sleep(10)
            
            #mqtt_client.publish("/" + location + "/" + room +":" , value)  
            #publish.single("/kids/yolo", "just do it", hostname=MQTT_HOST) 
            #publish.single("/" + location + "/" + room +"/"+sensor+":", value, hostname=MQTT_HOST)
            # publish multiple messages
            #publish.multiple(msgs, hostname=MQTT_HOST)
                 

            "node"
            {
                "location": "koti",
                "room": "olohuone",
                #"topic": topic,
                "value": value,
                "information": 
                {
                "node": "esp-01",
                "serialnumber": 1,
                }
            }

            i=i+1   

        mqtt_client.loop_stop()
        print("loop_stop") 

# mqtt_client.loop_forever()
    # def main()

if __name__ == "__main__":
    main() 