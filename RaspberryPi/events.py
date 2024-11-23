# Main program for Apex Entities's prototype

import RPi.GPIO as GPIO
from sense_hat import SenseHat
from enum import Enum
from time import sleep

sense = SenseHat()
sense.clear()

def PrintTitle():
    sense.clear()
    sense.show_message(
        "Apex Entities",
        scroll_speed=0.07,
        text_colour=[150,0,250]
        )
    sense.clear()

def PrintCreeper(delay):
    sense.clear()
    g = (0, 255, 0) # Green
    b = (0, 0, 0) # Black

    creeper_pixels = [
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, b, b, g, g, b, b, g,
        g, b, b, g, g, b, b, g,
        g, g, g, b, b, g, g, g,
        g, g, b, b, b, b, g, g,
        g, g, b, b, b, b, g, g,
        g, g, b, g, g, b, g, g
    ]

    sense.set_pixels(creeper_pixels)
    sleep(delay)
    sense.clear()

# pinctrl set 5 ip pn
# pinctrl set 6 ip pn
# pinctrl set 12 ip pn
# pinctrl -p

class State(Enum):
    Water = True
    Air = False

# Water Sensor 1
w1name = "1"
w1pin = 29
w1state = State.Water

# Water Sensor 2
w2name = "2"
w2pin = 31
w2state = State.Water

# Water Sensor 3
w3name = "3"
w3pin = 32
w3state = State.Water

# Count number of sensors underwater
count = 0

def StateToSting(state):
    str = ""
    if state == State.Water:
        str = "Water"
    else:
        str = "Air  "
    return str

def PrintSensors():
    global count
    count = int(w1state.value) + int(w2state.value) + int(w3state.value)
    print('%s=%s   %s=%s   %s=%s   Count=%s'% (
        w1name, StateToSting(w1state), 
        w2name, StateToSting(w2state), 
        w3name, StateToSting(w3state), 
        count))

def PrintCount():
    global count
    if count > 0:
        sense.show_letter(str(count))
    else:
        sense.clear()

def SetSensor1(channel):
    global w1state
    if GPIO.input(channel):
        w1state = State.Air
    else:
        w1state = State.Water
    PrintSensors()
    PrintCount()

def SetSensor2(channel):
    global w2state
    if GPIO.input(channel):
        w2state = State.Air
    else:
        w2state = State.Water
    PrintSensors()
    PrintCount()

def SetSensor3(channel):
    global w3state
    if GPIO.input(channel):
        w3state = State.Air
    else:
        w3state = State.Water
    PrintSensors()
    PrintCount()


# PrintTitle()

GPIO.setmode(GPIO.BOARD)

GPIO.setup(w1pin, GPIO.IN)
GPIO.setup(w2pin, GPIO.IN)
GPIO.setup(w3pin, GPIO.IN)

# Set initial states
SetSensor1(w1pin)
SetSensor2(w2pin)
SetSensor3(w3pin)
print('Ready')
# PrintCreeper(3)

GPIO.add_event_detect(w1pin, GPIO.BOTH, SetSensor1, bouncetime=200)
GPIO.add_event_detect(w2pin, GPIO.BOTH, SetSensor2, bouncetime=200)
GPIO.add_event_detect(w3pin, GPIO.BOTH, SetSensor3, bouncetime=200)



while True:
    pass