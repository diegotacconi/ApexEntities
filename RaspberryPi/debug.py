import RPi.GPIO as GPIO
from sense_hat import SenseHat
from time import sleep

# pinctrl -p
GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.IN) # GPIO5, pin29
GPIO.setup(31, GPIO.IN) # GPIO6, pin31
GPIO.setup(32, GPIO.IN) # GPI12, pin32

sense = SenseHat()


# LED Matrix
sense.clear()
sense.show_message(
    "Apex Entities",
    scroll_speed=0.07,
    text_colour=[150,0,250]
    )
sense.clear()


# Environmental Sensors
# humidity = sense.get_humidity()
# print("Humidity: %s %%rH" % humidity)

# temperature = sense.get_temperature()
# print("Temperature: %s C" % temperature)

# pressure = sense.get_pressure()
# print("Pressure: %s Millibars" % pressure)


g = (0, 255, 0) # Green
b = (0, 0, 0) # Black

creeper_pixels = [
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, b, b, g, g, b, b, g,
    g, b, b, g, g, b, b, g,
    g, g, g, b, b, g, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, g, g, b, g, g
]

sense.set_pixels(creeper_pixels)


sleep(5)
sense.clear()