import time
import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 60)
while True:
    for i in range(60):
        pixels[i] = (255, 0, 0)
        print(i)
        time.sleep(.1)
    i=0