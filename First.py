# import raspberry pi GPIO module
try:
    import RPi.GPIO as GPIO
    import time
except importError:
    print('ImportError!')
    exit()

try:
    GPI=[21,20,16,12,1,7,8,25]
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPI, GPIO.OUT)
    GPIO.output(GPI,0)
except:
    print('GPIO Init. error!')  
    exit()

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


print('Введите число (-1 для выхода)')
value = input()
try:
    o = int(value)
except ValueError:
    print('Это не похоже на число')
    exit()
except o==-1:
    exit()
except o<0 or 0>255:
    print('Chislo ne dolshno bit menshe 0 i bolshe 255')
    exit()
    value = o
num2dac(value)
    