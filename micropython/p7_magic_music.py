from microbit import *
import music

multiplier = 50

baseline_lightness = pin2.read_analog()

while True:
    lightness = pin2.read_analog()
    tone = baseline_lightness - lightness
    music.pitch(tone * multiplier)
    sleep(100)