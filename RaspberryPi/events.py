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

GPIO.setmode(GPIO.BOARD)

waterSensor1 = 29 # GPIO5, pin29
waterSensor2 = 31 # GPIO6, pin31
waterSensor3 = 32 # GPI12, pin32

GPIO.setup(waterSensor1, GPIO.IN)
GPIO.setup(waterSensor2, GPIO.IN)
GPIO.setup(waterSensor3, GPIO.IN)

waterSensorCount = 3

def PrintSensorState(channel):
    global waterSensorCount
    if GPIO.input(channel):
        print('%s is HIGH'%channel)
        waterSensorCount += 1
    else:
        print('%s is LOW'%channel)
        waterSensorCount = waterSensorCount - 1
    print('waterSensorCount is %s'%waterSensorCount)

# Print initial state
PrintSensorState(waterSensor1)
PrintSensorState(waterSensor2)
PrintSensorState(waterSensor3)

GPIO.add_event_detect(waterSensor1, GPIO.RISING, PrintSensorState, bouncetime=200)
GPIO.add_event_detect(waterSensor2, GPIO.RISING, PrintSensorState, bouncetime=200)
GPIO.add_event_detect(waterSensor3, GPIO.RISING, PrintSensorState, bouncetime=200)


while True:
    pass