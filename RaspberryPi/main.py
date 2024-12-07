# Main program for Apex Entities's prototype

import time
import RPi.GPIO as GPIO
from sense_hat import SenseHat, ACTION_RELEASED
from enum import Enum

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

def PrintReady(delay):
    sense.clear()
    o = (0, 0, 0)
    x = (0, 64, 0)
    X = (0, 255, 0)
    ready_pixels = [
        o, x, x, x, x, x, x, o,
        x, o, o, o, o, o, o, x,
        x, o, o, X, o, X, o, x,
        x, o, o, o, o, o, o, x,
        x, o, X, o, o, o, X, x,
        x, o, o, X, X, X, o, x,
        x, o, o, o, o, o, o, x,
        o, x, x, x, x, x, x, o
    ]
    sense.set_pixels(ready_pixels)
    time.sleep(delay)
    sense.clear()

def PrintExit(delay):
    sense.clear()
    o = (0, 0, 0)
    X = (128, 0, 0)
    ready_pixels = [
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, X, o, o, o, X, o,
        o, o, o, X, o, X, o, o,
        o, o, o, o, X, o, o, o,
        o, o, o, X, o, X, o, o,
        o, o, X, o, o, o, X, o,
        o, o, o, o, o, o, o, o
    ]
    sense.set_pixels(ready_pixels)
    time.sleep(delay)
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
    time.sleep(delay)
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

# Setup GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(w1pin, GPIO.IN)
GPIO.setup(w2pin, GPIO.IN)
GPIO.setup(w3pin, GPIO.IN)

# Set initial states
SetSensor1(w1pin)
SetSensor2(w2pin)
SetSensor3(w3pin)

# Detect GPIO events
GPIO.add_event_detect(w1pin, GPIO.BOTH, SetSensor1, bouncetime=200)
GPIO.add_event_detect(w2pin, GPIO.BOTH, SetSensor2, bouncetime=200)
GPIO.add_event_detect(w3pin, GPIO.BOTH, SetSensor3, bouncetime=200)

print('Ready')
PrintReady(1)

running = True
while running:
    for e in sense.stick.get_events():
    
        print('action=%s direction=%s'% (e.action, e.direction))

        if e.action == 'pressed' and e.direction == 'up':
            PrintReady(1)

        if e.action == 'pressed' and e.direction == 'down':
            PrintExit(1)
            print('Exit')
            sense.clear()
            running = False
            break

        if e.action == 'pressed' and e.direction == 'left':
            PrintTitle()

        if e.action == 'pressed' and e.direction == 'right':
            PrintCreeper(1)

        if e.action == 'pressed' and e.direction == 'middle':
            PrintSensors()
            PrintCount()
