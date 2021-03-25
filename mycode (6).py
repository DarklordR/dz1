# import raspberry pi GPIO module
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(1, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPI=[21,20,16,12,1,7,8,25]

#Функция lightUp(ledNumber, period), зажигающая светодиод, которая принимает в качестве аргументов номер светодиода ledNumber(от 0 до 7) и время горения в секундах - period. После вызова данной функции на плате должен загореться один светодиод под номером ledNumber и гореть в течение времени period. 

def lightUp(ledNumber, period):
    GPIO.setup(GPI[ledNumber], GPIO.OUT)
    GPIO.output(GPI[ledNumber], GPIO.HIGH)
    time.sleep(period)
    GPIO.cleanup()

#lightUp(4, 2)
#Функция blink(ledNumber, blinkCount, blinkPeriod), которая мигает заданное число раз одним светодиодом с заданным периодом времени. После вызова функции сначала должен загореться светодиод под номером ledNumber, через blinkPeriod секунд он должен потухнуть на то же количество секунд, затем этот процесс должен повториться blinkCount раз.

def blink(ledNumber, blinkCount, blinkPeriod):
    for i in range(0,blinkCount):
        GPIO.output(GPI[ledNumber],GPIO.HIGH)
        time.sleep(blinkPeriod)
        GPIO.output(GPI[ledNumber],0)
        time.sleep(blinkPeriod)

#blink(7, 3, 2)
#Функция runningLight(count, period), которая зажигает по порядку один светодиод за другим и гасит предыдущий, то есть это выглядит как один "бегущий" по кругу огонек. Параметр count задает количество повторений этой операции, period задает время горения светодиода. 
def runningLight(count, period):    
    for i in range(0,count):
        for j in range(0,8):
            GPIO.output(GPI[j],GPIO.HIGH)
            time.sleep(period)
            GPIO.output(GPI[j],0)
            
#runningLight(1, 3)
#Функция runningDark(count, period), которая делает практически то же самое, что и runningLight, но теперь "бежит" выключенный светодиод. То есть горят 7 огоньков, а восьмой, выключенный, перемещается.
def runningDark(count, period):    
    for i in range(0,count):
        GPIO.setmode(GPIO.BCM)
        for j in range(0,8):
            GPIO.output(GPI[j],GPIO.HIGH)
        
        for j in range(0,8):
            GPIO.output(GPI[j],0)
            time.sleep(period)
            GPIO.output(GPI[j],GPIO.HIGH)
    GPIO.cleanup()
    
#runningDark(1, 1)
#Функция decToBinList(decNumber), которая принимает десятичное число от 0 до 255, а возвращает это же число в двоичном виде в виде списка, длина которого равна 8, то есть числу светодиодов (например, если decNumber = 3, то результатом будет [0, 0, 0, 0, 0, 0, 1, 1]).
def decToBinList(decNumber):
    D = [0, 0, 0, 0, 0, 0, 0, 0]
    i = 0;
    while decNumber > 0:
        if (decNumber % 2 == 1):
            D[7-i] = 1
        decNumber = decNumber // 2    
        i+=1
    print(D)    
    return(D)               

#print(decToBinList(5))
#Функция lightNumber(number), которая принимает число от 0 до 255 в десятичном формате, переводит его в двоичный вид и зажигает только те светодиоды, номера которых соответствуют положению единиц в числе. Например, для числа 3 должны зажечься светодиоды под номерами 0 и 1. 
def lightNumber(decNumber): 
    D = decToBinList(decNumber)
    for j in range (0,8):
        if (D[j]==1):
            GPIO.output(GPI[j],GPIO.HIGH)

#lightNumber(245)
#Функция runningPattern(pattern, direction), которая циклично сдвигает "узор", соответсвующий числу pattern (от 0 до 255) в двоичном представлении, влево или вправо в зависимости от direction.  
def runningPattern(pattern, direction):
    D = decToBinList(pattern)
    a=0
    if (direction == 0): #left
        for i in range (0,7):
            GPI[i]=a
            GPI[i]=GPI[i+1]         
        GPI[7]=a    
    if (direction == 1): #right    
        for i in range (8,1):
            GPI[i]=a
            GPI[i]=GPI[i-1]
        GPI[0]=a        
    j = 0
    for j in range (0,8):
        if (GPI[j]==1):
            GPIO.output(GPI[j],GPIO.HIGH)
            
runningPattern(3,0)        


