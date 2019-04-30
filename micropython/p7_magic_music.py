from microbit import *
import music

multiplier = 20

baseline_lightness = pin2.read_analog()

while True:
    lightness = pin2.read_analog()
    tone = baseline_lightness - lightness
    if tone > 0:
        music.pitch(tone * multiplier)
    sleep(100)