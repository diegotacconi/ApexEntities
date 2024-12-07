# Main program for Apex Entities's prototype

import json
import requests
import time
import RPi.GPIO as GPIO
from sense_hat import SenseHat, ACTION_PRESSED
from enum import Enum

sense = SenseHat()
sense.clear()


data = {
    "WaterSensor1": True,
    "WaterSensor2": False,
    "WaterSensor3": True,
    "Temperature": 0,              # Temperature in degrees Celsius
    "Humidity": 0,                 # Relative humidity (RH) in percentage (%)
    "Pressure": 0,                 # Pressure in Millibars
    "OrientationPitch": 0,
    "OrientationRoll": 0,
    "OrientationYaw": 0,
    "GpsStatus": 3,                # 0=no gps, 1=no fix, 2=2D fix, 3=3D fix
    "GpsLatitude": 38.762393333,   # GPS Latitude in decimal degrees. Available when GpsStatus >= 2. Possible Values: -90.0 to 90.0
    "GpsLongitude": -94.665196667, # GPS Longitude in decimal degrees. Available when GpsStatus >= 2. Possible Values: -180.0 to 180.0
    "GpsAltitude": 322.9           # GPS Altitude in meters. Available when GpsStatus >= 3
}


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


def pushed_up(event):
    if event.action == ACTION_PRESSED:
        print('action=%s direction=%s'% (event.action, event.direction))
        PrintReady(1)

def pushed_down(event):
    global running
    if event.action == ACTION_PRESSED:
        print('action=%s direction=%s'% (event.action, event.direction))
        PrintExit(1)
        print('Exit')
        sense.clear()
        running = False

def pushed_left(event):
    if event.action == ACTION_PRESSED:
        print('action=%s direction=%s'% (event.action, event.direction))
        PrintTitle()

def pushed_right(event):
    if event.action == ACTION_PRESSED:
        print('action=%s direction=%s'% (event.action, event.direction))
        PrintCreeper(1)

def pushed_middle(event):
    if event.action == ACTION_PRESSED:
        print('action=%s direction=%s'% (event.action, event.direction))
        PrintSensors()
        PrintCount()


sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_middle = pushed_middle


def UpdateData():
    global data
    data['WaterSensor1'] = w1state.value
    data['WaterSensor2'] = w2state.value
    data['WaterSensor3'] = w3state.value
    data['Temperature'] = round(sense.get_temperature(), 2)
    data['Humidity'] = round(sense.get_humidity(), 2)
    data['Pressure'] = round(sense.get_pressure(), 2)


def PrintData():
    global data
    print(json.dumps(data, indent=3))


def PostData():
    startTime = time.time()
    global data
    url = "http://rhymescapes.net/fll_report_data/1"
    response = requests.post(url, data=data, timeout=5)
    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Error: {response.status_code}")
    endTime = time.time()
    print(f"PostData: {endTime - startTime} s")


print('Ready')
PrintReady(2)


running = True
while running:
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    UpdateData()
    PrintData()
    # PostData()
    time.sleep(1)
