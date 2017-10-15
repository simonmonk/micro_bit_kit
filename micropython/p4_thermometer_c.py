from microbit import *

while True:
    reading = pin1.read_analog()
    temp_c = reading * 0.075 - 17
    display.scroll(str(temp_c))
    