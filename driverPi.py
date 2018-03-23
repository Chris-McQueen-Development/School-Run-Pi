from grovepi import *

led = 2
pinMode(led,"OUTPUT")

while True:
    try:
        digitalWrite(led,1)
        
    except KeyboardInterrupt:
        digitalWrite(led,0)
        break
    except IOError:				
        print ("Error")