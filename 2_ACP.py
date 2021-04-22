import RPi.GPIO as GPIO
import time
 
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
        print ("Число должно быть от 0 до 255 (или -1 для выхода). Попробуйте еще раз.")
    return [(decNumber & (1 << i)) >> i for i in range (7, -1, -1)]
 
def num2dac (value):
    x = decToBinList (value)
    GPIO.output (out_list, tuple (x))
 
def V_search ():
    for dg in range (0, 256, 1):
        an = maxV * dg / 255
        num2dac(int(dg * 50 / 255))
        time.sleep (0.00001)
        if GPIO.input (In) == 0:
            print(outstr.format(digital = dg, analog = an))
            return dg

GPIO.output (v, 1)
while True:
    V_search()

GPIO.output (out_list, 0)
GPIO.output (V_chan, 0)
GPIO.cleanup (out_list)
GPIO.cleanup (v)
GPIO.cleanup (In)