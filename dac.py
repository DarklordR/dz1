import RPi.GPIO as GPIO

pins = [ 26, 19, 13, 6, 5, 11, 9, 10]

out  = [0] * 8


def clearLed():
    GPIO.output(pins, 0)

def WRITE(n_pin, value):
    GPIO.output(pins[n_pin], value)
    out[n_pin] = value 

def initGpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pins, GPIO.OUT)
    clearLed()

def resetGpio():
    clearLed()
    GPIO.cleanup()