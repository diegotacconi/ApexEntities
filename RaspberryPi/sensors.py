import json
import requests
import time
import RPi.GPIO as GPIO
from sense_hat import SenseHat
from enum import Enum

sense = SenseHat()
sense.clear()


# Environmental sensors
startTime = time.time()

temperature = sense.get_temperature()
humidity = sense.get_humidity()
pressure = sense.get_pressure()
sense.set_imu_config(False, False, True)  # gyroscope only
orientationPitch, orientationRoll, orientationYaw = sense.get_orientation().values()

endTime = time.time()
print(f"SensorsTime: {endTime - startTime} s")


# Json Data
data = {
    "WaterSensor1": True,
    "WaterSensor2": False,
    "WaterSensor3": True,
    "Temperature": round(temperature, 2),    # Temperature in degrees Celsius
    "Humidity": round(humidity, 2),          # Relative humidity (RH) in percentage (%)
    "Pressure": round(pressure, 2),          # Pressure in Millibars
    "OrientationPitch": round(orientationPitch, 2),
    "OrientationRoll": round(orientationRoll, 2),
    "OrientationYaw": round(orientationYaw, 2),
    "GpsStatus": 3,                # 0=no gps, 1=no fix, 2=2D fix, 3=3D fix
    "GpsLatitude": 38.762393333,   # GPS Latitude in decimal degrees. Available when GpsStatus >= 2. Possible Values: -90.0 to 90.0
    "GpsLongitude": -94.665196667, # GPS Longitude in decimal degrees. Available when GpsStatus >= 2. Possible Values: -180.0 to 180.0
    "GpsAltitude": 322.9           # GPS Altitude in meters. Available when GpsStatus >= 3
}

print(json.dumps(data, indent=3))
