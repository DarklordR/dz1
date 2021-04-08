# import raspberry pi GPIO module
import RPi.GPIO as GPIO
import time
import numpy as np
import matplotlib.pyplot as plt
from time import sleep

GPI=[21,20,16,12,1,7,8,25]
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPI, GPIO.OUT)
GPIO.output(GPI,0)

#Первый скрипт:
#При его запуске в терминале появляется запись "Введите число (-1 для выхода):". С клавиатуры вводится value от 0 до 255, после чего на ЦАП подается напряжение, пропорциональное этому числу. Для этого необходимо реализовать функцию num2dac(value), переводящую десятичное число в двоичное и зажигающую светодиоды в области DAC под номерами, соответствующими разрядам переданного числа, в которых стоят единицы. Проверка выходного напряжения должна проводиться с помощью мультиметра. После ввода числа снова появляется предложение ввести число (циклично).
one=0

def num2dac(value):
    GPIO.output(GPI,0)
    res = [0,0,0,0,0,0,0,0]
    for i in range(0,8):
        res[7 - i] = value & 1
        value = value >> 1
        if res[i]==1:
            GPIO.output(GPI[i], 1)
    time.sleep(0.01)  
    print(res)  

while one==1:
    print('Введите число (-1 для выхода)')
    value = int(input())
    if value ==-1: 
        exit(0)
    if (value<-1 or value>255):
        print('Error')
        exit(-1)   
    num2dac(value)
    
#Второй скрипт:
#При запуске появляется запись "Введите число повторений:", с клавиатуры вводится целое число repetitionsNumber, после чего на ЦАП подается напряжение, которое меняется в диапазоне возможных значений напряжения от минимума до максимума и обратно. Повторяется данный процесс repetitionsNumber раз. Вы можете повторно использовать функцию num2dac(value), если сделаете из первого скрипта модуль и подключите его в текущий скрипт.    
two=0

while two==1:
    print('Введите число повторений:')
    repetitionsNumber = int(input())
    for j in range(0,repetitionsNumber):
        for i in range(0,256):
            num2dac(i)
        for i in range(255,-1,-1):
            num2dac(i)
            
#Третий скрипт:
#При запуске этого скрипта на ЦАП подается напряжение, которое меняется по синусоидальному закону в течение времени time. Здесь необходимо создать ndarray (массив) целых чисел, которые будут соответствовать значениям функции синуса, меняющейся с частотой frequency. На выходе ЦАП каждые 1/samplingFrequency секунд выставляется новое напряжение, соответствующее значению функции синуса в данный момент времени. Прежде чем передавать синусоидальный сигнал на ЦАП, нужно нарисовать график и проверить, что сигнал имеет нужную форму, амплитуду, максимальное и минимальное значения в нужном диапазоне.  
def sinus(time,frequency,samplingFrequency):
  t = np.arange(0, time, frequency)
  ndarray = np.sin(t)
  plt.plot(t, ndarray)
  plt.title('Синус')
  plt.xlabel('Время')
  plt.ylabel('Амплитуда sin(t)')
  plt.show()  
  
  for i in range(0, len(ndarray), 1):
    ndarray[i]= (ndarray[i]+1)*255/2

  for i in range(0, len(ndarray), 1):
    GPIO.output(GPI,0)
    res = [0,0,0,0,0,0,0,0]
    for g in range(0,8):
        res[7 - g] = ndarray[i] & 1
        ndarray[i] = ndarray[i] >> 1
        if res[g]==1:
            GPIO.output(GPI[i], 1)
    time.sleep(1/samplingFrequency)

sinus(10,0.1,0)