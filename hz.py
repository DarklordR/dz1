# import raspberry pi GPIO module
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPI=[24,25,8,7,12,16,20,21]

GPIO.output(GPI,0)

#Функция lightUp(ledNumber, period), зажигающая светодиод, которая принимает в качестве аргументов номер светодиода ledNumber(от 0 до 7) и время горения в секундах - period. После вызова данной функции на плате должен загореться один светодиод под номером ledNumber и гореть в течение времени period. 
def lightUp(ledNumber, period):
    GPIO.output(GPI[ledNumber], GPIO.HIGH)
    time.sleep(period)
    GPIO.output(GPI[ledNumber], 0)
    GPIO.cleanup()

#lightUp(7, 2)
#Функция blink(ledNumber, blinkCount, blinkPeriod), которая мигает заданное число раз одним светодиодом с заданным периодом времени. После вызова функции сначала должен загореться светодиод под номером ledNumber, через blinkPeriod секунд он должен потухнуть на то же количество секунд, затем этот процесс должен повториться blinkCount раз.

def blink(ledNumber, blinkCount, blinkPeriod):
    for i in range(0,blinkCount):
        GPIO.output(GPI[ledNumber],GPIO.HIGH)
        time.sleep(blinkPeriod)
        GPIO.output(GPI[ledNumber],0)
        time.sleep(blinkPeriod)

#blink(7, 10, 0.1)
#Функция runningLight(count, period), которая зажигает по порядку один светодиод за другим и гасит предыдущий, то есть это выглядит как один "бегущий" по кругу огонек. Параметр count задает количество повторений этой операции, period задает время горения светодиода. 
def runningLight(count, period):    
    for i in range(0,count):
        for j in range(0,8):
            GPIO.output(GPI[j],GPIO.HIGH)
            time.sleep(period)
            GPIO.output(GPI[j],0)
            
#runningLight(3, 0.1)
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
    
#runningDark(3, 0.1)
#Функция decToBinList(decNumber), которая принимает десятичное число от 0 до 255, а возвращает это же число в двоичном виде в виде списка, длина которого равна 8, то есть числу светодиодов (например, если decNumber = 3, то результатом будет [0, 0, 0, 0, 0, 0, 1, 1]).
def decToBinList(number):
    res = [0,0,0,0,0,0,0,0]
    for i in range(0,8):
        res[i] = number & 1
        number = number >> 1
    return res            

#print(decToBinList(5))
#Функция lightNumber(number), которая принимает число от 0 до 255 в десятичном формате, переводит его в двоичный вид и зажигает только те светодиоды, номера которых соответствуют положению единиц в числе. Например, для числа 3 должны зажечься светодиоды под номерами 0 и 1. 
def lightNumber(number):
    bin = decToBinList(number)
    for i in range(8):
        GPIO.output(GPI[i], bin[i])
    time.sleep(1)
    for i in GPI:
        GPIO.output(i, 0)    

#lightNumber(3)
#Функция runningPattern(pattern, direction), которая циклично сдвигает "узор", соответсвующий числу pattern (от 0 до 255) в двоичном представлении, влево или вправо в зависимости от direction.  
def runningPattern(pattern, direction):
    for i in range(8):
        lightNumber(pattern)

        if direction == 0:
            high_bit = (pattern & 128) >> 7
            pattern = (pattern << 1) + high_bit
        else:
            low_bit = pattern & 1
            pattern = (pattern >> 1) + (low_bit << 7)

            
runningPattern(5,0) 