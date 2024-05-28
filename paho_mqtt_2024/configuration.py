#!/usr/bin/ python3

# ********************* configuratrion.py **************************************
#
#   Description:        Configuraions for mqtt to google-sheet gateway
#
#   Dependencies:       Install with pip3:  paho-mqtt, google-api-python-client, google-auth-oauthlib

"""-------- Version history ----------------------------------------------------

    
    v0.1    yasperzee   5'23   

#TODO:
-----------------------------------------------------------------------------"""

""" Select some Topics to subscribe or add your ownones
"$SYS/#"
"Demo/#"
"Demo/Movable/#"
"Koti/#"
"Koti/Liikkuva/#"
"Koti/Olohuone/#"
"Koti/Olohuone/Lampotila"
"Koti/Olohuone/Ilmankosteus"
"Koti/Olohuone/Ilmanpaine"
"Koti/Olohuone/Korkeus"
"Koti/Olohuone/Valoisuus"
"Koti/Olohuone/NodeInfo"  # To find correct sheet on spreadsheet
"Koti/Olohuone/TopicInfo" # Location of the node
"""

#SUBS = "SLEEP_TESTING"
SUBS = "SUBSALL"

if SUBS == "SLEEP_TESTING":
    subscription = (
        "Koti/Testing/TopicInfo",       # NODE-00 / BMP280
        "Koti/Testing/NodeInfo",
        "Koti/Testing/Lampotila",
        "Koti/Testing/Ilmanpaine",
        "Koti/Testing/Korkeus",
        "Koti/Testing/Vcc"
        )
else:
    subscription = (
        "Koti/IceBox/NodeInfo",       # NODE-01 / DHT22 (ESP01)
        "Koti/IceBox/TopicInfo",
        "Koti/IceBox/Lampotila",
        "Koti/IceBox/Ilmankosteus",
        "Koti/Partsi/NodeInfo",     # NODE-02 / BMP180 (ESP01)
        "Koti/Partsi/TopicInfo",
        "Koti/Partsi/Lampotila",
        "Koti/Partsi/Ilmanpaine",
        "Koti/Partsi/Korkeus",
        "Koti/Olohuone/NodeInfo",   # NODE-04 / BMP280 & TEMT6000 (ESP12E)
        "Koti/Olohuone/TopicInfo",
        "Koti/Olohuone/Lampotila",
        "Koti/Olohuone/Ilmanpaine",
        "Koti/Olohuone/Korkeus",
        "Koti/Olohuone/Valoisuus"
        )


#MQTT_CLIENT_ID = "MqttClient_W530"
MQTT_CLIENT_ID = "MqttClient_RPI3"
#MQTT_CLIENT_ID = "MqttClient_N510"
#MQTT_CLIENT_ID = "SleepTest_"
#MQTT_CLIENT_ID = "Docker 01"

#Select port
#TCP/IP port 1883 is reserved with IANA for use with MQTT.
#TCP/IP port 8883 is also registered, for using MQTT over SSL.
MQTT_PORT = 1883
#MQTT_PORT = 8883
MQTT_KEEPALIVE = 60 # Seconds 0..120
MQTT_RECONN_DELAY = 30 # Seconds 0..120

try:
    MQTT_CLIENT_ID
except NameError:
    print('ERROR: MQTT_CLIENT_ID not defined')
    quit()


ERROR_VALUE = -999,9

