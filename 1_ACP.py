import RPi.GPIO as GPIO
import time

outstr = "{digital} = {analog}V"
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
 
GPIO.output (v, 1)
while True:
    value = int(input ("Введите число (-1 для выхода): "))
    if value < -1 or value > 255:
        print ("Необходимо ввести число [0;255]! Попробуйте еще раз:")
    else:
        if value == -1:
            break
        an = maxV * value / 255.0
        print (outstr.format(digital = value, analog = an))
        num2dac(int(value * 50 / 255))

GPIO.output (out_list, 0)
GPIO.output (v, 0)
GPIO.cleanup (out_list)
GPIO.cleanup (v)
GPIO.cleanup (In)