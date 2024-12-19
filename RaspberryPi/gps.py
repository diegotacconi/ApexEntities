#!/usr/bin/env python3
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
    print(" Time: " + str(packet.time))

else:
    print(" Latitude: NOT AVAILABLE")
    print(" Longitude: NOT AVAILABLE")
    print(" Time: NOT AVAILABLE")


if packet.mode >= 3:
    print(" Altitude: " + str(packet.alt))
else:
    print(" Altitude: NOT AVAILABLE")


print()
