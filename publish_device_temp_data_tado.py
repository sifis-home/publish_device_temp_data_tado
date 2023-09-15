# -*- coding: utf-8 -*-

import websocket
import time
import random
import json
import os
import subprocess
import _thread
import rel
import argparse
import datetime
import hashlib
import re
import socket
from PyTado.interface import Tado

parser = argparse.ArgumentParser(description='')
parser.add_argument('--requestor_type', help='Requestor Type', required=True, type=str)

args = parser.parse_args()
requestor_type = args.requestor_type
print("Requestor Type: ", requestor_type)

t = Tado('my@username.com', 'mypassword')

def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### Connection closed ###")


def on_open(ws):
    print("### Connection established ###")

def publish():

    ## getting the hostname by socket.gethostname() method
    hostname = socket.gethostname()
    ## getting the IP address using socket.gethostbyname() method
    ip_address = socket.gethostbyname(hostname)
    ## printing the hostname and ip_address
    print(f"Hostname: {hostname}")
    print(f"IP Address: {ip_address}")

    requestor_id = ip_address

    # Get current date and time
    now = datetime.datetime.now()

    # Generate a random hash using SHA-256 algorithm
    hash_object = hashlib.sha256()
    hash_object.update(bytes(str(now), 'utf-8'))
    hash_value = hash_object.hexdigest()

    # Concatenate the time and the hash
    request_id = str(requestor_id) + str(now) + hash_value
    request_id = re.sub('[^a-zA-Z0-9\n\.]', '', request_id).replace('\n', '').replace(' ', '')


    ws = websocket.WebSocketApp("ws://localhost:3000/ws",
                                on_open=on_open,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever(dispatcher=rel)  # Set dispatcher to automatic reconnection
    rel.signal(2, rel.abort)  # Keyboard Interrupt

    # Initialize an empty list to store random numbers
    temperature = []

    while True:
        # # Generate a random number between 1 and 100 (you can adjust the range as needed)
        # random_number = random.randint(1, 100)
        # print(f"Random Number: {random_number}")

        # # Add the random number to the list
        # temperature.append(random_number)

        climate = t.get_climate(zone=1)
        print(f"Temperature: {climate['temperature']}")
        
        # Add the random number to the list
        temperature.append(climate['temperature'])
        
        # Print the list as a string after 48 seconds
        if len(temperature) == 48:

            temperature_string_list = []

            temperature_string = str(temperature).replace("[", "").replace("]", "")
            temperature_string_list.append(temperature_string)
            
            print("List of temperatures:", temperature_string_list)

            ws_req = {
                    "RequestPostTopicUUID": {
                        "topic_name": "SIFIS:Privacy_Aware_Device_Anomaly_Detection",
                        "topic_uuid": "Anomaly_Detection",
                        "value": {
                            "description": "Device Anomaly Detection",
                            "requestor_id": str(requestor_id),
                            "requestor_type": str(requestor_type),
                            "request_id": str(request_id),
                            "connected": True,
                            "Data Type": "List",
                            "Temperatures": temperature_string_list
                        }
                    }
                }
            ws.send(json.dumps(ws_req))
            
            # Empty the list
            temperature = []
        
        # Wait for one second before generating the next random number
        time.sleep(1)
publish()