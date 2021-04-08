from   num2dac import num2dac
from   dac     import *
import numpy as np
from time import sleep
from math import sin, pi
import matplotlib
import matplotlib.pyplot as plt


def CreateSine(frequency, time, samplingFrequency):
    omega = 2 * pi * frequency
    times = [0] * (samplingFrequency * time + 1)
    for i in range(1, len(times)):
        times[i] = times[i-1] + (1 / samplingFrequency)
    values = times.copy()
    for i in range(len(values)):
        values[i] = sin(times[i] * omega)
    #print(values)
    plt.grid()
    plt.scatter(times, values)
    plt.show()
    
    delay = 1/float(samplingFrequency)

    for x in values:
        num2dac(int(255 * x))
        sleep(delay)
    

def main():
    initGpio()
    frequency = int(input("Частота: "))
    time      = int(input("Время: "))
    sample    = int(input("Частота дискретизации: "))
    CreateSine(frequency, time, sample)
    resetGpio()

main()