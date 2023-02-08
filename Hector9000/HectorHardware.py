#!/usr/bin/env python3
# -*- coding: utf8 -*-
##
#   HectorHardware.py       API class for Hector9000 hardware
#


# imports
from __future__ import division
from fileinput import close

from time import sleep, time
import sys
import math

from Hector9000.utils import HectorAPI as api
from Hector9000.conf import HectorConfig

# hardware modules
import Adafruit_PCA9685
import RPi.GPIO as GPIO
from Hector9000.conf.HX711_Python3.hx711 import HX711
GPIO.setwarnings(False)	

# settings

# Uncomment to enable debug output:
import logging

# initialization
logging.basicConfig(level=logging.CRITICAL)

VERBOSE_LEVEL = 0


def log(message):
    if VERBOSE_LEVEL == 0:
        logging.log(VERBOSE_LEVEL, "" + str(message))


def error(message):
    if VERBOSE_LEVEL < 3:
        print("Hardware ERROR: " + str(message))


def warning(message):
    if VERBOSE_LEVEL < 2:
        print("Hardware WARNING: " + str(message))


class HectorHardware(api.HectorAPI):

    def __init__(self, cfg):

        log("initialization HectorHardware")

        self.config = cfg
        
        GPIO.setmode(GPIO.BOARD)
        
   
        # setup scale (HX711)
        self.hx = HX711(dout_pin=40, pd_sck_pin=38)
        self.hx.zero()
        ratio = cfg["hx711"]["ref"]
        self.hx.set_scale_ratio(ratio) 
        #print(self.hx.get_weight_mean(20))
        

        # setup servos (PCA9685)
        self.valveChannels = self.config["pca9685"]["valvechannels"]
        self.numValves = len(self.valveChannels)
        self.valvePositions = cfg["pca9685"]["valvepositions"]
        self.fingerChannel = cfg["pca9685"]["fingerchannel"]
        self.fingerPositions = cfg["pca9685"]["fingerpositions"]
        self.lightPin = cfg["pca9685"]["lightpin"]
        self.lightChannel = cfg["pca9685"]["lightpwmchannel"]
        self.lightPositions = cfg["pca9685"]["lightpositions"]
        pcafreq = cfg["pca9685"]["freq"]
        self.pca = Adafruit_PCA9685.PCA9685()
        self.pca.set_pwm_freq(pcafreq)

        GPIO.setup(self.lightPin, GPIO.OUT)

        #setup water pump
        self.bomba=cfg["bomba"]["PUMP"]
        GPIO.setup(self.bomba,GPIO.OUT)
        # setup air pump (GPIO) con control por PWM
        self.pump = cfg["pump"]["MOTOR"]
        GPIO.setup(self.pump, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pump,3000) 


    def getConfig(self):
        return self.config

    def light_on(self):
        log("turn on light")
        GPIO.setup(self.lightPin, GPIO.OUT)
        GPIO.output(self.lightPin, False)

    def light_off(self):
        log("turn off light")
        GPIO.setup(self.lightPin, GPIO.OUT)
        GPIO.output(self.lightPin, True)

    def scale_readout(self):
        weight = self.hx.get_weight_mean(1)
        print(weight)
        return weight

    def scale_tare(self):
        print("scale tare")
        self.hx.zero()

    #Water's pump activation and deactivation
    def bomba_start(self):
        print("Empezo")
        GPIO.setup(self.bomba,GPIO.OUT)
        GPIO.output(self.bomba,True)

    def bomba_stop(self):
        print("Paro")
        GPIO.setup(self.bomba, GPIO.OUT)
        GPIO.output(self.bomba,False)
    
    #Pump's activaction and deactivation
    def pump_start(self):
        print("start pump")
        self.pwm.start(100)
        # GPIO.setup(self.pump, GPIO.OUT)
        # GPIO.output(self.pump,True)

    
    def pump_medium(self):
        print("medium pump")
        self.pwm.start(65)

    def pump_stop(self):
        log("stop pump")
        # GPIO.setup(self.pump, GPIO.OUT)
        # GPIO.output(self.pump,False)
        self.pwm.start(0)

    def valve_open(self, index, open=1):
        if open == 0:
            log("close valve")
        else:
            log("open valve")
        if (index < 0 and index >= len(self.valveChannels) - 1):
            return
        if open == 0:
            log("close valve no. %d" % index)
        else:
            log("open valve no. %d" % index)
        ch = self.valveChannels[index]
        pos = self.valvePositions[index][1 - open]
        log("ch %d, pos %d" % (ch, pos))
        self.pca.set_pwm(ch, 0, pos)

    def valve_close(self, index):
        print("close valve")
        self.valve_open(index, open=0)

    def valve_dose(
            self,
            index,
            amount,
            timeout=30,
            cback=None,
            progress=(
                0,
                100),
            topic=""):
        log("dose channel %d, amount %d" % (index, amount))
        if index < 0 and index >= len(self.valveChannels) - 1:
            return -1
        #if not self.arm_isInOutPos():
            #return -1
        t0 = time()
        balance = True

        if (index!=10):
            self.valve_close(10)
            sleep(0.5)
        if amount <= 30:
            porcentaje = amount * 0.3
        elif amount >30 and amount <= 75: 
            porcentaje = amount * 0.45
        elif amount > 75 and amount <= 90:
            porcentaje = amount * 0.55
        elif amount > 90 and amount <= 120:
            porcentaje = amount * 0.75

        a= math.pow(amount,5)
        b= math.pow(amount,4)
        c= math.pow(amount,3)
        d= math.pow(amount,2)

        print(amount)
        final_amount = (-0.000000002*a)+(0.0000004*b)-(0.00003*c)+(0.0017*d)+(0.8638*amount)-3.1837
        final_amount=round(final_amount)
    
        print(final_amount)
        self.scale_tare()
        sr = self.scale_readout()
        self.light_on()
        self.pump_start()
        self.valve_open(index)
        self.bomba_start()
        if balance and sr < -1.5 and sr > -5:
            amount = amount + sr
            balance = False
        last_over = False
        last = sr
        while True:
            sr = self.scale_readout()
            if sr < -1 and sr > -5:
                warning("weight abnormality: scale balanced")
                amount = amount + sr
                # balance = False
            
            if sr<porcentaje:
                self.pump_start()
            elif sr > porcentaje:
                self.pump_medium()

            if sr >= final_amount:
                if last_over:
                    print("dosing complete")
                    break
                else:
                     last_over = True
            else:
                last_over = False
            log("Read scale: %d" % sr)
            if (sr - last) > 5:
                log("reset timeout")
                t0 = time()
                last = sr
            if (time() - t0) > timeout:
                error("timeout reached")
                self.pump_stop()
                self.valve_close(index)
                if cback:
                    cback(progress[0] + progress[1])
                return False
            sleep(0.1)   
        self.pump_stop()      
        self.valve_close(index)
        self.bomba_stop()  
        if(index != 10):
            self.valve_close(10)
            sleep(0.5)
        self.light_off()
        if cback:
            cback(progress[0] + progress[1])
        log("completed reset after dosing")
        return True

    def finger(self, pos=0):
        self.pca.set_pwm(self.fingerChannel, 0, self.fingerPositions[pos])

    def ping(self, num, retract=True, cback=None):
        log("ping")
        self.pca.set_pwm(self.fingerChannel, 0, self.fingerPositions[1])
        for i in range(num):
            self.pca.set_pwm(self.fingerChannel, 0, self.fingerPositions[1])
            sleep(.15)
            self.pca.set_pwm(self.fingerChannel, 0, self.fingerPositions[2])
            sleep(.15)
        if retract:
            self.pca.set_pwm(self.fingerChannel, 0, self.fingerPositions[1])
        else:
            self.pca.set_pwm(self.fingerChannel, 0, self.fingerPositions[0])

    def cleanAndExit(self):
        log("Cleaning...")
        GPIO.cleanup()
        log("Bye!")
        sys.exit()

    # Helper function to make setting a servo pulse width simpler.
    def set_servo_pulse(self, channel, pulse):
        pulse_length = 1000000  # 1,000,000 us per second
        pulse_length //= 60  # 60 Hz
        log('{0} µs per period'.format(pulse_length))
        pulse_length //= 4096  # 12 bits of resolution
        log('{0} µs per bit'.format(pulse_length))
        pulse *= 1000
        pulse //= pulse_length
        self.pca.set_pwm(channel, 0, pulse)

# end class HectorHardware

def main():
    co= HectorConfig.config
    h=HectorHardware(co)
    h.bomba_stop()
    # h.scale_tare()
    # h.light_on()
    # h.valve_open(11,1)
    # sleep(3)
    # h.valve_open(11,0)
    # sleep(0.5)
    # h.light_off()
    # h.valve_dose(7,30,30)
    # while True:
    #       h.bomba_start()
        # h.scale_readout()
        # h.pump_start()
if __name__ == "__main__":
    main()