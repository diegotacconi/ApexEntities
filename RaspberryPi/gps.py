#!/usr/bin/env python3
# Further information at https://github.com/MartijnBraam/gpsd-py3/blob/master/DOCS.md

import gpsd
import json
import logging
import time
from sense_hat import SenseHat, ACTION_PRESSED

sense = SenseHat()
sense.clear()


data = {
    "GpsStatus": 3,                # 0=no gps, 1=no fix, 2=2D fix, 3=3D fix
    "GpsLatitude": 32.89823,       # GPS Latitude in decimal degrees. Available when GpsStatus >= 2. Possible Values: -90.0 to 90.0
    "GpsLongitude": -97.1115,      # GPS Longitude in decimal degrees. Available when GpsStatus >= 2. Possible Values: -180.0 to 180.0
    "GpsAltitude": 322.9           # GPS Altitude in meters. Available when GpsStatus >= 3
}


logging.basicConfig(
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S',
    format='%(asctime)s.%(msecs)03d | %(levelname)-8s | %(message)s',
    handlers=[
        #logging.FileHandler("/var/tmp/apex.log", mode='w'),
        logging.StreamHandler()
    ]
)


def PrintScrollingMessage(msg):
    sense.clear()
    sense.show_message(msg, scroll_speed=0.03)
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


def pushed_down(event):
    global running
    if event.action == ACTION_PRESSED:
        logging.info('Joystick: %s-%s event'% (event.action, event.direction))
        logging.info('Exit')
        PrintExit(1)
        sense.clear()
        running = False


def pushed_right(event):
    if event.action == ACTION_PRESSED:
        logging.info('Joystick: %s-%s event'% (event.action, event.direction))
        PrintGpsStatus()


# Detect Joystick events
sense.stick.direction_down = pushed_down
sense.stick.direction_right = pushed_right


# Default Values
gpsStatus = -1





def PrintGpsStatus():
    msg = f"GPS: {gpsStatus}"
    logging.info(msg)
    PrintScrollingMessage(msg)


def UpdateGps():
    global data
    global gpsStatus
    try:

        gpsStatus = -2

        data['GpsStatus'] = gpsStatus
        data['GpsLatitude'] = 11
        data['GpsLongitude'] = 12
        data['GpsAltitude'] = 13
        return gpsStatus

    except:
        return gpsStatus

    '''
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
    '''



def PrintData():
    global data
    # logging.info(json.dumps(data, indent=3))
    logging.info(json.dumps(data))


running = True
while running:
    UpdateGps()
    PrintData()
    time.sleep(2)
