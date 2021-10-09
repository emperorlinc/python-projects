from random import choice
from time import sleep
from pyfiglet import figlet_format
from termcolor import colored

display = figlet_format("mobile number generator 1000")
header = colored(display, color="magenta", on_color="on_yellow", attrs=["blink"])
print(header)
sleep(3)


def suffix():
    nums = choice(range(00000000, 99999999))
    nums = str(nums)
    return nums


class PhoneNumbers:

    def etisalat(self):
        count = 0
        total = input("HOW MANY PHONE NUMBERS DO YOU WANNA GENERATE? ")
        total = int(total)
        while count < total:
            prefix = "0909"
            result = prefix + suffix()
            print("GENERATING 9MOBILE NUMBERS...")
            sleep(1)
            print(result)
            count += 1

    def glo(self):
        count = 0
        total = input("HOW MANY PHONE NUMBERS DO YOU WANNA GENERATE? ")
        total = int(total)
        while count < total:
            prefix = "0815"
            result = prefix + suffix()
            print("GENERATING GLO NUMBERS...")
            sleep(1)
            print(result)
            count += 1

    def mtn(self):
        count = 0
        total = input("HOW MANY PHONE NUMBERS DO YOU WANNA GENERATE? ")
        total = int(total)
        while count < total:
            prefix = "0708"
            result = prefix + suffix()
            print("GENERATING MTN NUMBERS...")
            sleep(1)
            print(result)
            count += 1

    def airtel(self):
        count = 0
        total = input("HOW MANY PHONE NUMBERS DO YOU WANNA GENERATE? ")
        total = int(total)
        while count < total:
            prefix = "0802"
            result = prefix + suffix()
            print("GENERATING AIRTEL NUMBERS...")
            sleep(1)
            print(result)
            count += 1


x = PhoneNumbers()
request = input("WHICH NIGERIA NETWORK DO YOU WANT TO EXTRACT ").lower()
if request == "airtel":
    x.airtel()
elif request == "glo":
    x.glo()
elif request == "etisalat" or request == "9mobile":
    x.etisalat()
elif request == "mtn":
    x.mtn()
else:
    print("INPUT A CORRECT NIGERIA NETWORK NAME")





















