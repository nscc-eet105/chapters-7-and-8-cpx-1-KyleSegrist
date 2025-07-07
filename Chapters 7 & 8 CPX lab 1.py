# Kyle Segrist
# Chapters 7 & 8 cpx lab-1
# Light pattern from file

from adafruit_circuitplayground import cp
import time
import random

OFF = (0, 0, 0)
TIME = 0.1  # Time in seconds

#PATTERN = [0, 5, 1, 6, 2, 7, 3, 8, 4, 9]
light_pattern = []


with open("pixel_pattern.txt") as file:
    for line in file:
        line=line.replace("\n","")
        light_pattern.append(int(line))

# generate a random color using RGB spectrum
def pixel_color():
    red=random.randint(0, 255)
    green=random.randint(0, 255)
    blue=random.randint(0, 255)
    return (red, green, blue)

def main():
    while True:
        for pixel in light_pattern:
            cp.pixels[pixel] = pixel_color()
            time.sleep(TIME)
            cp.pixels[pixel] = OFF
            time.sleep(TIME)


main()

