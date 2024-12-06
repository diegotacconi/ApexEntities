import json
import requests
import time
import RPi.GPIO as GPIO
from sense_hat import SenseHat, ACTION_RELEASED
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


def UpdateSensorsData():
    startTime = time.time()
    global data
    temperature = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()
    data['Temperature'] = round(temperature, 2)
    data['Humidity'] = round(humidity, 2)
    data['Pressure'] = round(pressure, 2)
    endTime = time.time()
    print(f"UpdateSensorsData: {endTime - startTime} s")


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


def pushed_down(event):
    global running
    if event.action != ACTION_RELEASED:
        print('Exit (Joystick pushed down event)')
        running = False


sense.stick.direction_down = pushed_down


running = True
while running:
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    UpdateSensorsData()
    PrintData()
    PostData()
    time.sleep(5)
