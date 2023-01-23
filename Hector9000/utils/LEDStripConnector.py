from Hector9000.utils.LEDStripAPI import LEDStripAPI
import time
import board
import neopixel
import random
import itertools as it


class LEDStripConnector(LEDStripAPI):

    def __init__(self):
        self.PORT = board.D18
        self.NUM = 201
        self.NUMBASE = 4
        self.pixels = neopixel.NeoPixel(self.PORT, self.NUM)
        self.cols = [
            (0, 218, 255),
            (235,132, 255),
            (135,255,211),
            (245,255,84)
        ]
        # Colores para 1
        self.colores1 = [
            (150,255,46),
            (46,255,197),
            (121,88,255),
            (255,90,251)
        ]
        #Colores para 2
        self.colores2 = [
            (255,251,0),
            (0,255,220),
            (255,156,0),
            (213,0,255),
        ]
        #Colores de la malla
        self.malla=(91,154,255)
        self.col_neutral = (80, 80, 30)
        self.NUMCOLS = len(self.cols)
        self.NUMCOLORES1= len(self.colores1)
        self.mode = 1
        self.ORDER = neopixel.GRB
        self.num_pixels = self.NUM
        self.pixels.fill(self.col_neutral)
        self.drinkcolor = (0, 0, 0)


    
#Funcion para prender los servo motores
    def servos(self,servo):
        if servo =="1":
           self.mode=10
           if self.mode == 10:
                while True:
                    for i in it.chain(range(44,59),range(77,201)):
                        self.pixels[i] = self.malla
                    for c in range(self.NUMCOLORES1):
                        for i in range(59,77):
                            self.pixels[i] = self.colores2[c]
                            time.sleep(0.025)
                    if self.mode != 10:
                        break
        if servo == "2":
            self.mode=20

    def standby(self, color=(80, 80, 30), type=0):
        if type == 0:
            self.pixels.fill(color)
        else:
            self.pixels.fill((0, 0, 0))



    def drinkfinish(self, color=(255, 255, 255), type=0):
        self.finish(color, type)

    def finish(self, color=(255, 255, 255), type=0):
        for i in range(0,31):
            self.pixels[i] = (color[0], color[1], color[2])
        # self.pixels.show()
        # for i in range(10):
        #     time.sleep(0.05)
        #     self.pixels[14 - i] = color
        #     self.pixels.show()
        # for i in range(3):
        #     for j in range(self.NUMBASE):
        #         self.pixels[j] = color
        #     self.pixels.show()
        #     time.sleep(0.05)
        #     for j in range(self.NUMBASE):
        #         self.pixels[j] = (0, 0, 0)
        #     self.pixels.show()
        #     time.sleep(0.05)
        # self.mode = 3

    def drinkloop(self):
        print("drinkloop")
        for i in range(self.NUMBASE):
            self.pixels[i] = self.drinkcolor
            self.pixels.show()
        for i in range(5):
            start = random.randrange(9, 14)
            print(start)
            for j in range(3):
                start = start - j
                for index in range(10):
                    index = index + 5
                    if index is start:
                        self.pixels[index] = self.drinkcolor
                    else:
                        self.pixels[index] = (0, 0, 0)
                if self.mode == 99:
                    self.pixels.show()
                    time.sleep(0.3)
                else:
                    return


    def led_loop(self):
        #Mode inicial
        if self.mode == 1:
            self.mode1()
        elif self.mode == 2:
            self.mode2()
        elif self.mode == 3:
            self.mode3()
        elif self.mode == 4:
            self.mode4()
        elif self.mode == 5:
            self.standart()
        elif self.mode == 6:
            self.standart()
        elif self.mode == 7:
            self.standart()
        elif self.mode == 8:
            self.standart()
        elif self.mode == 9:
            self.standart()
        elif self.mode == 10:
            self.standart()
        elif self.mode == 11:
            self.standart()
        elif self.mode == 12:
            self.standart()
        elif self.mode == 13:
            self.standart()
        #Mode para cuando esta la maquina sin hacer nada
        elif self.mode == 14:
            self.standart()
        #Mode para cuando el id sea par
        elif self.mode == 15:
            self.dosedrink(0)
        #Mode para cuando el id sea impar
        elif self.mode == 16:
            self.dosedrink(1)
        elif self.mode == 99:
            self.drinkloop()

    def loop(self):
        self.led_loop()

    
    
    #Funcion estandar de inicio del programa
    def mode1(self):
        for i in range(self.NUMCOLS):
            self.pixels.fill(self.cols[i])
            for j in range(4):
                if self.mode == 1:
                    time.sleep(1)
                else:
                    return

    # Funcion estandar que pasa en la maquina mientras no hace ninguna bebida
    def standart(self):
            print("Estamos en standart 0")
            for c in range(self.NUMCOLS):
                self.pixels.fill(self.colores2[c])
                time.sleep(15)


    #Funcion para los cocteles la parte de adelante, obtiene la funcion segun el id
    def dosedrink(self,type):
        if type == 0:
            for i in range(0,15):
                self.pixels[i]=(76,50,255)
            for i in range(29,44):
                self.pixels[i]=((255,90,251))
            for c in range(self.NUMCOLORES1):
                for i in range(15,29):
                    self.pixels[i] = self.colores1[c]
                    time.sleep(0.01)

        elif type == 1:
            for i in range(0,15):
                self.pixels[i]=(255,90,251)
            for i in range(29,44):
                self.pixels[i]=(76,50,255)
            for c in range(self.NUMCOLORES1):
                for i in range(15,29):
                    self.pixels[i] = self.colores2[c]
                    time.sleep(0.01)


    def mode2(self):
        self.pixels.fill((255, 0, 0))
        # time.sleep(.05)
        # self.pixels.fill((255, 255, 255))
        # time.sleep(.05)

    def mode3(self):
        for i in range(0,240):
            self.pixels[i] = (0, 0, 255)             

    def wheel(self, pos):
        if pos < 0 or pos > 255:
            r = g = b = 0
        elif pos < 85:
            r = int(pos * 3)
            g = int(255 - pos * 3)
            b = 0
        elif pos < 170:
            pos -= 85
            r = int(255 - pos * 3)
            g = 0
            b = int(pos * 3)
        else:
            pos -= 170
            r = 0
            g = int(pos * 3)
            b = int(255 - pos * 3)
        return (
            r,
            g,
            b) if self.ORDER == neopixel.RGB or self.ORDER == neopixel.GRB else (
            r,
            g,
            b,
            0)

    def rainbow_cycle(self, wait):
        for j in range(255):
            for i in range(self.NUM - self.NUMBASE):
                pixel_index = (i * 256 // self.num_pixels) + j
                self.pixels[self.NUMBASE + i] = self.wheel(pixel_index & 255)
            for j in range(self.NUMBASE):
                self.pixels[j] = self.pixels[self.NUMBASE]
            self.pixels.show()
            time.sleep(wait)

    def mode4(self):
        for i in range(4):
            self.rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step


def main():
    test = LEDStripConnector()

    while 1:
        # test.finish((123, 0, 0),0)
        test.mode3()
        


if __name__ == "__main__":
    main()


