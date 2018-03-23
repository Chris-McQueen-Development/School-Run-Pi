from grovepi import *
import time
import grovepi
import requests
import json


led = 2
pinMode(led,"OUTPUT")

light_sensor = 0
threshold = 10
grovepi.pinMode(light_sensor,"INPUT")

numberOfFreeSeats = 3;
while True:
    sensor_value = grovepi.analogRead(light_sensor)

        # Calculate resistance of sensor in K
    resistance = (float)(1023 - sensor_value) * 10 / sensor_value

    if resistance > threshold:
            # Send HIGH to switch on LED
        r = requests.get('https://school-run-451c2.firebaseio.com/schools.json')
        #data = r.json()
        payload = r.json()
        currentFreeSeats = payload['jesmond-high']['spaces']
        newFreeSeats = currentFreeSeats + numberOfFreeSeats
        
        payload['jesmond-high']['spaces'] = newFreeSeats
        print(json.dumps(payload))
        
        put = requests.put("https://school-run-451c2.firebaseio.com/schools.json", data=json.dumps(payload))
        print(put.text)
        grovepi.digitalWrite(led,1)
    else:
            # Send LOW to switch off LED
        grovepi.digitalWrite(led,0)
        print("sensor_value = %d resistance = %.2f" %(sensor_value,  resistance))
        time.sleep(.2)