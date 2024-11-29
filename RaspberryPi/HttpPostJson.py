import json
 
# Data to be written
data = {
    "WaterSensor1": True,
    "WaterSensor2": False,
    "WaterSensor3": True,
    "Temperature": 29.3, # Temperature in degrees Celsius
    "Humidity": 70.0, # Relative humidity (RH) in percentage (%)
    "Pressure": 1013.25, # Pressure in Millibars
    "OrientationPitch": 0,
    "OrientationRoll": 0,
    "OrientationYaw": 0,
}
 
# Serializing json
dataJson = json.dumps(data, indent=4)
 
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(dataJson)

print(dataJson)

