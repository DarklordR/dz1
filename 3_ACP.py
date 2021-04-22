import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

outstr = "Digital value: {digital}, analog value: {analog} V"
maxV = 3.3

out_list = (26, 19, 13, 6, 5, 11, 9, 10)
In = 4
v = 17
GPIO.setmode (GPIO.BCM)
GPIO.setup (out_list, GPIO.OUT)
GPIO.setup (v, GPIO.OUT)
GPIO.setup (In, GPIO.IN)
 
 
def decToBinList (decNumber):
    if decNumber < 0 or decNumber > 255:
        raise ValueError
    return [(decNumber & (1 << i)) >> i for i in range (7, -1, -1)]
 
def num2dac (value):
    x = decToBinList (value)
    GPIO.output (out_list, tuple (x))
 
def V_search ():
    dg = 0
    i = 128
    while i >= 1:
        num2dac(int((dg + i) * 50 / 255))
        time.sleep (0.00001)
        if GPIO.input (in_chan) == 1:
            dg += i
        i = int(i / 2)
    an = maxV * dg / 255
    print(outstr.format(digital = dg, analog = an))
    return dg

GPIO.output (V_chan, 1)
while True:
        V_search()

GPIO.output (out_list, 0)
GPIO.output (V, 0)
GPIO.cleanup (out_list)
GPIO.cleanup (v)
GPIO.cleanup (In)