from microbit import *

def read_temp_c():
    reading = pin1.read_analog()
    temp_c = round(reading * 0.157 - 54)
    return temp_c

set_temp = read_temp_c() + 2
   
while True:
    if button_a.was_pressed():
        set_temp -= 1
        display.scroll('Set' + str(set_temp))
    elif button_b.was_pressed():
        set_temp += 1
        display.scroll('Set' + str(set_temp))
    display.scroll(str(read_temp_c()))
    if read_temp_c() > set_temp:
        pin0.write_digital(1)
    else:
        pin0.write_digital(0)