import json
 
# Data to be written
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
    "GpsLatitude": 38.762393333,   # GPS Latitude in Decimal Degrees
    "GpsLongitude": -94.665196667, # GPS Longitude in Decimal Degrees
    "GpsAltitude": 322.9           # GPS Altitude in Meters
}
 
# Serializing json
dataJson = json.dumps(data, indent=4)
 
# Writing to json file

with open("RaspberryPi/example.json", "w") as outfile:
    outfile.write(dataJson)

# print(dataJson)

