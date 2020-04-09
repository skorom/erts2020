from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
message = ""

def update_temperature():
    #Gets the current temperature in degrees Celsius from the humidity sensor.
    temp = sense.get_temperature()
    print("Temperature: %s C" % temp)    

def update_humidity():
    #Gets the percentage of relative humidity from the humidity sensor.
    humidity = sense.get_humidity()
    print("Humidity: %s %%rH" % humidity)

def update_pressure():
    #Gets the current pressure in Millibars from the pressure sensor.
    pressure = sense.get_pressure()
    print("Pressure: %s Millibars" % pressure)

def update_orientation():
    #Gets the current orientation in degrees using the aircraft principal axes of pitch, roll and yaw.
    orientation = sense.get_orientation_degrees()
    print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))

    
while(True):
    update_temperature()
    update_humidity()
    update_pressure()
    update_orientation()
    sleep(10)


#JoyStick
############################################################################
""" x = 3
y = 3
sense = SenseHat()

def clamp(value, min_value=0, max_value=7):
    return min(max_value, max(min_value, value))

def pushed_up(event):
    global y
    if event.action != ACTION_RELEASED:
        y = clamp(y - 1)

def pushed_down(event):
    global y
    if event.action != ACTION_RELEASED:
        y = clamp(y + 1)

def pushed_left(event):
    global x
    if event.action != ACTION_RELEASED:
        x = clamp(x - 1)

def pushed_right(event):
    global x
    if event.action != ACTION_RELEASED:
        x = clamp(x + 1)

def refresh():
    sense.clear()
    sense.set_pixel(x, y, 255, 255, 255)

sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_any = refresh
refresh()
pause() """
############################################################################
#Led Matrix

""" sense = SenseHat()
sense.show_message("One small step for Pi!", text_colour=[255, 0, 0]) """

############################################################################

""" X = [255, 0, 0]  # Red
O = [255, 255, 255]  # White

question_mark = [
O, O, O, X, X, O, O, O,
O, O, X, O, O, X, O, O,
O, O, O, O, O, X, O, O,
O, O, O, O, X, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, X, O, O, O, O
]

sense.set_pixels(question_mark) """
############################################################################
""" temp = sense.get_temperature()
print("Temperature: %s C" % temp)

# alternatives
print(sense.temp)
print(sense.temperature) """

# Documenatation: https://pythonhosted.org/sense-hat/api/#sense-hat-api-reference