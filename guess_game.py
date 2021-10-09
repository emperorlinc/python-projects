import random
import pyfiglet
from termcolor import colored
header = pyfiglet.figlet_format("GUESS GAME 1000")
header = colored(header, color="magenta", on_color="on_red", attrs=["blink"])
print(header)
def gamebody():
    rand_num = random.randint(1, 10)
    guess = None
    while guess != rand_num:
        guess = input(f"MAKE A GUESS FROM 1 TO 10: ")
        guess = int(guess)
        if rand_num > guess:
            print("TOO LOW...")
        elif rand_num < guess:
            print("TOO HIGH...")
        elif guess == str(""):
            print("INVALID GUESS...")
        else:
            print("CORRECT!!!")
            play_again = input("DO YOU WANNA CONTINUE WITH THE GAME? (y/n) ")
            if play_again == "y":
                rand_num = random.randint(1, 10)
                guess = None
            elif play_again == "n":
                print("THANK YOU... BYE!!!")
                print("***GRANDMASTER***\n")
                break
            else:
                print('TYPE EITHER "Y" OR "N"')
gamebody()