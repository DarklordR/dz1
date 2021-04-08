# import raspberry pi GPIO module
try:
    import RPi.GPIO as GPIO
    import time
except importError:
    print('ImportError!')
    exit()

try:
    GPI=[10,9,11,5,6,13,19,26]
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPI, GPIO.OUT)
    GPIO.output(GPI,0)
except:
    print('GPIO Init. error!')  
    exit()


def num2dac(value):
    GPIO.output(GPI,0)
    res = [0,0,0,0,0,0,0,0]
    for i in range(0,8):
        res[i] = value & 1
        value = value >> 1
        if res[i]==1:
            GPIO.output(GPI[i], 1)
    time.sleep(0.001) 

try:
    while True:
        try:
                value = int(input('Введите число (-1 для выхода):'))
                if value < -1 or value > 255:
                    print ('Chislo ne dolshno bit menshe 0 i bolshe 255!')
                    continue
        except ValueError:
            print('Это не похоже на число!')
        else:
            if value == -1:
                break
            for j in range(0,value):
                for i in range(0,256):
                    num2dac(i)
                for i in range(255,-1,-1):
                    num2dac(i)
except:
    print('Unknown Mistake')
finally:
    GPIO.output(GPI,0)
    GPIO.cleanup(GPI)       
