from grovepi import *
import time
import grovepi

led = 2
pinMode(led,"OUTPUT")

light_sensor = 0
threshold = 10
grovepi.pinMode(light_sensor,"INPUT")


while True:
    sensor_value = grovepi.analogRead(light_sensor)

        # Calculate resistance of sensor in K
    resistance = (float)(1023 - sensor_value) * 10 / sensor_value

    if resistance > threshold:
            # Send HIGH to switch on LED
        grovepi.digitalWrite(led,1)
    else:
            # Send LOW to switch off LED
        grovepi.digitalWrite(led,0)

    print("sensor_value = %d resistance = %.2f" %(sensor_value,  resistance))
    time.sleep(.5)