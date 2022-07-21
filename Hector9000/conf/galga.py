import RPi.GPIO as gpio
import time

DT =6
SCK=5

sample=0

val=0

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(SCK, gpio.OUT)

def readCount():
  i=0
  Count=0
  gpio.setup(DT, gpio.OUT)
  gpio.output(DT,1)
  gpio.output(SCK,0)
  gpio.setup(DT, gpio.IN)

  while gpio.input(DT) == 1:
      i=0
  for i in range(24):
        gpio.output(SCK,1)
        Count=Count<<1

        gpio.output(SCK,0)
        time.sleep(0.001)
        if gpio.input(DT) == 0: 
            Count=Count+1
        
  gpio.output(SCK,1)
  Count=Count
  gpio.output(SCK,0)
  return Count

while 1:
  count= readCount()
  w=0
  w=(count-sample)/106
  print (w,"g")
  
time.sleep(0.5)
    