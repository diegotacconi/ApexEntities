import RPi.GPIO as GPIO
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

# pinctrl set 5 ip pn
# pinctrl set 6 ip pn
# pinctrl set 12 ip pn
# pinctrl -p
# ---
# 29: ip    pn | lo // GPIO5 = input
# 31: ip    pn | lo // GPIO6 = input
# 32: ip    pn | lo // GPIO12 = input
# ---
# 29: ip    pn | hi // GPIO5 = input
# 31: ip    pn | hi // GPIO6 = input
# 32: ip    pn | hi // GPIO12 = input

w1name = "A"
w1pin = 29
w1state = False

w2name = "B"
w2pin = 31
w2state = False

w3name = "C"
w3pin = 32
w3state = False

count = 0

def PrintSensors():
    global count
    count = int(w1state) + int(w2state) + int(w3state)
    print('%s=%s   %s=%s   %s=%s   Count=%s'% (w1name, int(w1state), w2name, int(w2state), w3name, int(w3state), count))

def PrintCount():
    global count
    if count > 0:
        sense.show_letter(str(count))
    else:
        sense.clear()

def SetSensor1(channel):
    global w1state
    if GPIO.input(channel):
        w1state = True
    else:
        w1state = False
    PrintSensors()
    PrintCount()

def SetSensor2(channel):
    global w2state
    if GPIO.input(channel):
        w2state = True
    else:
        w2state = False
    PrintSensors()
    PrintCount()

def SetSensor3(channel):
    global w3state
    if GPIO.input(channel):
        w3state = True
    else:
        w3state = False
    PrintSensors()
    PrintCount()

GPIO.setmode(GPIO.BOARD)

GPIO.setup(w1pin, GPIO.IN)
GPIO.setup(w2pin, GPIO.IN)
GPIO.setup(w3pin, GPIO.IN)

# Set initial states
SetSensor1(w1pin)
SetSensor2(w2pin)
SetSensor3(w3pin)
print('Ready')

GPIO.add_event_detect(w1pin, GPIO.RISING, SetSensor1, bouncetime=200)
GPIO.add_event_detect(w2pin, GPIO.RISING, SetSensor2, bouncetime=200)
GPIO.add_event_detect(w3pin, GPIO.RISING, SetSensor3, bouncetime=200)

while True:
    pass