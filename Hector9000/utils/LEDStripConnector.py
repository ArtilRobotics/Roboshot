from Hector9000.utils.LEDStripAPI import LEDStripAPI
import time
import board
import neopixel
import random
import itertools as it


class LEDStripConnector(LEDStripAPI):

    def __init__(self):
        self.PORT = board.D18
        self.NUM = 203
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
            (36,249,255),
            (220,89,255),
            (218,124,255),
        ]
        #Colores para funcion estandar
        self.colores2 = [
            (0,194,255),
            (225,0,255),
        ]

        #Colores para los servos
        self.colorservos = [
            (0,134,255),
            (225,0,196),
        ]
        #Colores de la malla
        self.malla=(138,159,255)

        self.col_neutral = (80, 80, 30)
        self.NUMCOLS = len(self.cols)
        self.NUMCOLORES1= len(self.colores1)
        self.NUMCOLORES2= len(self.colores2)
        self.NUMSERVOS= len(self.colorservos)
        self.mode = 1
        self.ORDER = neopixel.GRB
        self.num_pixels = self.NUM
        self.pixels.fill(self.col_neutral)
        self.drinkcolor = (0, 0, 0)

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
        print(self.mode)
        #Mode inicial
        if self.mode == 1:
            self.mode1()
        # #Mode servo 0
        # elif self.mode == 2:
        #     self.servos(0)
        #     self.dosedrink()
        # elif self.mode == 3:
        #     self.servos(1)
        #     # self.dosedrink()
        # elif self.mode == 4:
        #     self.servos(2)
        #     self.dosedrink()
        # elif self.mode == 5:
        #     self.servos(3)
        #     self.dosedrink()
        # elif self.mode == 6:
        #     self.servos(4)
        #     self.dosedrink()
        # elif self.mode == 7:
        #     self.servos(5)
        #     self.dosedrink()
        # elif self.mode == 8:
        #     self.servos(6)
        #     self.dosedrink()
        # elif self.mode == 9:
        #     self.servos(7)
        #     self.dosedrink()
        # elif self.mode == 10:
        #     self.servos(8)
        #     self.dosedrink()
        # elif self.mode == 11:
        #     self.servos(9)
        #     self.dosedrink()
        # elif self.mode == 12:
        #     self.servos(10)
        #     self.dosedrink()
        # elif self.mode == 13:
        #     self.servos(11)
        #     self.dosedrink()
        # #Mode para cuando esta la maquina sin hacer nada
        # elif self.mode == 14:
        #     self.standart()
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
            for c in range(self.NUMCOLORES1):
                self.pixels.fill(self.colores1[c])
                time.sleep(15)


    #Funcion para los cocteles la parte de adelante, obtiene la funcion segun el id
    def dosedrink(self,type=1):
        if type == 0:
                self.pixels.show()
                for c in range(self.NUMCOLORES2):
                    for i in range(15,31):
                        self.pixels[i] = self.colores2[c]
                        time.sleep(0.025)
                # for i in it.chain(range(0,15),range(29,44)):
                #     self.pixels[i]=(255,0,255)

        elif type == 1:
            # self.pixels.show()
            for c in range(self.NUMCOLORES2):
                for i in range(15,29):
                    self.pixels[i] = self.colores2[c]
                    time.sleep(0.025)

    #Funcion para prender los servo motores
    def servos(self,servo):
        if servo == 0:
            for i in it.chain(range(46,91),range(109,203)):
                for c in range(self.NUMSERVOS):
                    for i in range(91,109):
                        self.pixels.fill(self.colorservos[c])
                        time.sleep(0.025)
                self.pixels.fill(255,0,0)
        elif servo == 1:
            print("Entre al servo 1")
            for c in range(self.NUMSERVOS):
                for i in it.chain(range(15,31),range(61,79)):
                    self.pixels[i]=(self.colorservos[c])
                    time.sleep(0.005)
                
        elif servo == 2:
            for i in it.chain(range(44,101),range(104,107),range(110,134),range(146,201)):
                self.pixels.fill(self.malla)
            for c in range(self.NUMSERVOS):
                for i in it.chain(range(101,104),range(134,146),range(107,110)):
                    self.pixels.fill(self.colorservos[c])
                    time.sleep(0.25)
        elif servo == 3:
            for i in it.chain(range(44,164),range(167,170),range(173,179)):
                self.pixels.fill(self.malla)
            for c in range(self.NUMSERVOS):
                for i in it.chain(range(164,167),range(170,173),range(179,201)):
                    self.pixels.fill(self.colorservos[c])
                    time.sleep(0.25)
        elif servo == 4:
            for i in it.chain(range(44,137),range(140,167),range(179,201)):
                self.pixels.fill(self.malla)
            for c in range(self.NUMSERVOS):
                for i in it.chain(range(167,179),range(137,140)):
                    self.pixels.fill(self.colorservos[c])
                    time.sleep(0.25)
        elif servo == 5:
            for i in it.chain(range(44,198),range(101,143),range(158,201)):
                self.pixels.fill(self.malla)
            for c in range(self.NUMSERVOS):
                for i in it.chain(range(143,158),range(98,101)):
                    self.pixels.fill(self.colorservos[c])
                    time.sleep(0.25)
        elif servo == 6:
            for i in it.chain(range(44,80),range(83,86),range(89,104),range(116,201)):
                self.pixels.fill(self.malla)
            for c in range(self.NUMSERVOS):
                for i in it.chain(range(104,116),range(80,83),range(86,89)):
                    self.pixels.fill(self.colorservos[c])
                    time.sleep(0.25)
        elif servo == 7:
            for i in it.chain(range(44,53),range(59,74),range(86,201)):
                self.pixels.fill(self.malla)
            for c in range(self.NUMSERVOS):
                for i in it.chain(range(53,59),range(74,86)):
                    self.pixels.fill(self.colorservos[c])
                    time.sleep(0.25)
        elif servo == 8:
            for i in it.chain(range(44,71),range(74,77),range(80,113),range(125,201)):
                self.pixels.fill(self.malla)
            for c in range(self.NUMSERVOS):
                for i in it.chain(range(113,125),range(71,74),range(77,80)):
                    self.pixels.fill(self.colorservos[c])
                    time.sleep(0.25)
        elif servo == 9:
            for i in it.chain(range(53,83),range(92,201)):
                self.pixels.fill(self.malla)
            for c in range(self.NUMSERVOS):
                for i in it.chain(range(44,53),range(83,92)):
                    self.pixels.fill(self.colorservos[c])
                    time.sleep(0.25)
        elif servo == 10:
            for i in it.chain(range(44,110),range(113,116),range(119,125),range(137,201)):
                self.pixels.fill(self.malla)
            for c in range(self.NUMSERVOS):
                for i in it.chain(range(125,137),range(110,113),range(116,119)):
                    self.pixels.fill(self.colorservos[c])
                    time.sleep(0.25)
        elif servo == 11:
            for i in it.chain(range(44,140),range(143,146),range(149,158),range(170,201)):
                self.pixels.fill(self.malla)
            for c in range(self.NUMSERVOS):
                for i in it.chain(range(158,170),range(146,149),range(140,143)):
                    self.pixels.fill(self.colorservos[c])
                    time.sleep(0.25)
    
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

    def mode3(self):
        while True:
            for c in range(self.NUMCOLS):
                for i in range(self.NUM - self.NUMBASE):
                    self.pixels[self.NUMBASE + i] = self.cols[c]
                    if self.mode == 1:
                        time.sleep(.025)

def main():
    test = LEDStripConnector()

    while 1:
        # test.finish((123, 0, 0),0)
        test.standart()
        


if __name__ == "__main__":
    main()


