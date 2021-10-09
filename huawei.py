import time
from pyfiglet import figlet_format
from termcolor import colored


def delay():
    total = range(1, 31, -1)
    for i in total:
        gen = yield i
        loc = iter(gen)
        sleep(1)
        next(loc)


hold = delay()

boot_display = figlet_format("HUAWEI Y9")
colored(boot_display, color="white", on_color="on_yellow", attrs=["bold"])
print(boot_display)
print("BOOTING... BOOTING... BOOTING...")
security = input("whats your password: ").lower()
if security == "linc":
    pass
else:
    print("incorrect password... try again in 30sec")
    print(next(hold))


home = input("WHAT CAN I HELP YOU WITH==> ").lower()
if home in ("image", "images", "pictures", "picture", "photos", "photo"):
    print(ascii("i don't have any image now but, do you like this smile :-)"))
