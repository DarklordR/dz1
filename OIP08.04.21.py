# import raspberry pi GPIO module
import RPi.GPIO as GPIO
import time
#import numpy as np
#import matplotlib.pyplot as plt
#from time import sleep

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
    
    value = input()
    try:
        o = int(value)
    except ValueError:
        print("Это не похоже на число")
        continue
    if o==-1:
        exit()
    if o<0:
        print("Число не может быть отрицательным")
        continue
    num2dac(value)
    
#Второй скрипт:
#При запуске появляется запись "Введите число повторений:", с клавиатуры вводится целое число repetitionsNumber, после чего на ЦАП подается напряжение, которое меняется в диапазоне возможных значений напряжения от минимума до максимума и обратно. Повторяется данный процесс repetitionsNumber раз. Вы можете повторно использовать функцию num2dac(value), если сделаете из первого скрипта модуль и подключите его в текущий скрипт.    
two=0

while two==1:
    #import(num2dac)
    print('Введите число повторений (-1 - выход):')
    repetitionsNumber = input()
    try:
        o = int(repetitionsNumber)
    except ValueError:
        print("Это не похоже на число")
        continue
    if o==-1:
        exit()
    if o<0:
        print("Число повторений не может быть отрицательным")
        continue
    
    for j in range(0,o):
        for i in range(0,256):
            num2dac(i)
        for i in range(255,-1,-1):
            num2dac(i)
            
#Третий скрипт:
#При запуске этого скрипта на ЦАП подается напряжение, которое меняется по синусоидальному закону в течение времени time. Здесь необходимо создать ndarray (массив) целых чисел, которые будут соответствовать значениям функции синуса, меняющейся с частотой frequency. На выходе ЦАП каждые 1/samplingFrequency секунд выставляется новое напряжение, соответствующее значению функции синуса в данный момент времени. Прежде чем передавать синусоидальный сигнал на ЦАП, нужно нарисовать график и проверить, что сигнал имеет нужную форму, амплитуду, максимальное и минимальное значения в нужном диапазоне.  
tre=0

while tre==1:
time,frequency,samplingFrequency
    print('Введите время (-1 - выход):')
    repetitionsNumber = input()
    try:
        k = int(repetitionsNumber)
    except ValueError:
        print("Это не похоже на число")
        continue
    if k==-1:
        exit()
    if k<0:
        print("Время не может быть отрицательным")
        continue
    time = k;
    
    print('Введите частоту графика (-1 - выход):')
    frequency = input()
    try:
        k = int(frequency)
    except ValueError:
        print("Это не похоже на число")
        continue
    if k==-1:
        exit()
    if k<0:
        print("Частота не может быть отрицательной")
        continue
    frequency = k;
    
    print('Введите частоту моргания (-1 - выход):')
    samplingFrequency = input()
    try:
        k = int(samplingFrequency)
    except ValueError:
        print("Это не похоже на число")
        continue
    if k==-1:
        exit()
    if k<0:
        print("Частота не может быть отрицательной")
        continue
    samplingFrequency = k;
    
  t = np.arange(0, k, frequency)
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