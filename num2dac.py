from dac import *

def dec2bin(dec_number):
    bits = []
    while dec_number > 0:
        bits.append(dec_number & 0b1)
        dec_number = dec_number >> 1
    return bits

def num2dac(dec_number):
    clearLed()
    bits = dec2bin(dec_number)
    for i in range(len(bits)): WRITE(7 - i, bits[i])

def main():
    
    initGpio()

    while True:
        try:
            print("Введите число: ", end="")
            
            try: 
                number = int(input())
            except ValueError:
                print("Некорректное число")
                continue

            if not 0 <= number < 256:
                print("Некорректное число")
                continue

            num2dac(number)

        except KeyboardInterrupt:
            print("\nСпасибо за использование!")
            resetGpio()
            quit()

if __name__ == "__main__":
    main()