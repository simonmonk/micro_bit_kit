from microbit import *
import music

z = accelerometer.get_z()

while True:
    if accelerometer.get_z() < z - 50:
        music.play(music.BA_DING)