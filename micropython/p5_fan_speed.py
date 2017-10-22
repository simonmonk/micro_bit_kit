from microbit import *

min_power = 300
max_power = 1023
power_step = (max_power - min_power) / 9
speed = 0

def set_power(speed):
    display.show(str(speed))
    if speed == 0:
        pin0.write_analog(0)
    else:
        pin0.write_analog(speed * power_step + min_power)
   
set_power(speed)
   
while True:
    if button_a.was_pressed():
        speed -= 1
        if speed < 0:
            speed = 0
        set_power(speed)
    elif button_b.was_pressed():
        speed += 1
        if speed > 9:
            speed = 9
        set_power(speed)
    sleep(100)