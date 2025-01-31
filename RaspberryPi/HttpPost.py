import json
import requests
 
data = {
    "WaterSensor1": True,
    "WaterSensor2": False,
    "WaterSensor3": True,
    "Temperature": 29.3,           # Temperature in degrees Celsius
    "Humidity": 70.0,              # Relative humidity (RH) in percentage (%)
    "Pressure": 1013.25,           # Pressure in Millibars
    "OrientationPitch": 0,
    "OrientationRoll": 0,
    "OrientationYaw": 0,
    "GpsStatus": 3,                # 0=no gps, 1=no fix, 2=2D fix, 3=3D fix
    "GpsLatitude": 38.762393333,   # GPS Latitude in decimal degrees. Available when GpsStatus >= 2. Possible Values: -90.0 to 90.0
    "GpsLongitude": -94.665196667, # GPS Longitude in decimal degrees. Available when GpsStatus >= 2. Possible Values: -180.0 to 180.0
    "GpsAltitude": 322.9           # GPS Altitude in meters. Available when GpsStatus >= 3
}

url = "http://rhymescapes.net/fll_report_data/1"
response = requests.post(url, data=data, timeout=5)

# Check response status code
if response.status_code == 200:
    print(response.text)
else:
    print(f"Error: {response.status_code}")
