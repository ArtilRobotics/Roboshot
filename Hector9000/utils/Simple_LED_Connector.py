from Hector9000.utils.LEDStripAPI import LEDStripAPI
import time
import board
import neopixel
import threading


class Simple_LED_Connector(LEDStripAPI):

    def __init__(self):
        self.PORT = board.D18
        self.NUM = 240
        self.NUMBASE = 5
        self.pixels = neopixel.NeoPixel(self.PORT, self.NUM)
        self.cols = [
            (255, 0, 0),
            (255, 63, 0),
            (255, 120, 0),
            (0, 255, 0),
            (0, 255, 255),
            (0, 0, 255),
            (255, 0, 255)
        ]
        self.col_neutral = (80, 80, 30)
        self.NUMCOLS = len(self.cols)
        self.mode = 1
        self.ORDER = neopixel.GRB
        self.num_pixels = self.NUM
        self.pixels.fill(self.col_neutral)
        self.drinkcolor = (0, 0, 0)
        self.thr = threading.Thread(target=self.mode3, args=())
        self.thr.start()

    def standart(self, color=(80, 80, 30), type=0):
        return

    def standby(self, color=(80, 80, 30), type=0):
        return

    def dosedrink(self, color=(0, 0, 255), type=0):
        return

    def drinkfinish(self, color=(255, 255, 255), type=0):
        print("drinkfinish in connector")
        self.mode = 2
        self.finish(color, type)
        self.mode = 1
        print("finished animation")

    def finish(self, color=(255, 255, 255), type=0):
        print("in finish")
        time.sleep(0.1)
        self.pixels.fill((0, 0, 0))
        # self.pixels.show()
        print("filled")
        for i in range(60):
            time.sleep(0.08)
            self.pixels[59 - i] = color
        # self.pixels.show()
        for i in range(3):
            for j in range(self.NUMBASE):
                self.pixels[j] = color
            # self.pixels.show()
            time.sleep(0.02)
            for j in range(self.NUMBASE):
                self.pixels[j] = (0, 0, 0)
            # self.pixels.show()
            time.sleep(0.1)
        print("after finish")

    # mode 1: Farben Rad
    # mode 2: Drinkfinish

    def loop(self):
        pass

    def mode3(self):
        for i in range(188,201):
            self.pixels[i] = (0, 0, 255)
            time.sleep(0.75)
        while True:
            for c in range(self.NUMCOLS):
                for i in range(self.NUM - self.NUMBASE):
                    self.pixels[self.NUMBASE + i] = self.cols[c]
                    if self.mode == 1:
                        time.sleep(.025)
                    else:
                        print("stopped animation")
                        while not self.mode == 1:
                            pass
                        print("continued animation")
                        for i in range(self.NUMBASE):
                            self.pixels[i] = (0, 0, 255)
                        break

def main():
    h=Simple_LED_Connector()
    while 1:
        # h.finish((123, 0, 0),0)
        h.mode3()
        
if __name__ == "__main__":
    main()