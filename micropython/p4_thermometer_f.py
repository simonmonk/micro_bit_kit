from microbit import *

while True:
    reading = pin1.read_analog()
    temp_c = round(reading * 0.135 +1)
    display.scroll(str(temp_c))