#!/usr/bin/env python3
# Remember to install 'pip3 install gpsd-py3'
# Further information at https://github.com/MartijnBraam/gpsd-py3/blob/master/DOCS.md

import gpsd

# Connect to the local gpsd
gpsd.connect()

# Get gps position
packet = gpsd.get_current()

# Print data
print()
print(" Device: " + str(gpsd.device()))
print(" Mode: " + str(packet.mode))
print(" Satellites: " + str(packet.sats))

if packet.mode >= 2:
    print(" Latitude: " + str(packet.lat))
    print(" Longitude: " + str(packet.lon))
    print(" Track: " + str(packet.track))
    print(" Horizontal Speed: " + str(packet.hspeed))
    print(" Time: " + str(packet.time))
    print(" Error: " + str(packet.error))
else:
    print(" Latitude: NOT AVAILABLE")
    print(" Longitude: NOT AVAILABLE")
    print(" Track: NOT AVAILABLE")
    print(" Horizontal Speed: NOT AVAILABLE")
    print(" Time: NOT AVAILABLE")
    print(" Error: NOT AVAILABLE")

if packet.mode >= 3:
    print(" Altitude: " + str(packet.alt))
    print(" Climb: " + str(packet.climb))
else:
    print(" Altitude: NOT AVAILABLE")
    print(" Climb: NOT AVAILABLE")

print()
