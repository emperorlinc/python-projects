from pyfiglet import figlet_format
from time import sleep
# from terminal import render


class RoboCop:

    def __init__(self, name,  battery=100, battery_low=30, intro="I am Robo2000, i have unlimited skill, the more i'm updated the better i become"):
        self.name = name
        self.battery = battery
        self.intro = intro
        self.battery_low = battery_low

    def battery_life(self):
        return f"Battery life is now remaining {self.battery}%"

    def write(self):
        """whenever any task is being called on or a skill is being initiated, it reduces the battery life"""
        text = figlet_format(input("input your text in here: "))
        self.battery -= 50
        return text

    def speak(self):
        self.battery -= 20
        return figlet_format("Remember that there no other person that can be you better than you already are")

    def charge(self):
        while True:
            self.battery += 1
            sleep(2)
            print(self.battery)
            if self.battery == 100:
                print("Battery fully charged")
                break

    def battery_low(self, charge):
        start_charge = charge()
        if battery >= 30:
            print("Battery running low, initializing optimum power saving mode")
        return start_charge

    # if self.battery_low:
    #     charge()


trial = RoboCop("Robo2000")
print(trial.name)
print(trial.speak())
print(trial.write())
print(trial.battery_low)
# print(trial.play_game())
# request = str(input("What do you want Robo2000 to do for you: "))

if __name__ == "__main__":
    while True:
        request = str(input("What do you want Robo2000 to do for you: "))
        if request == "write":
            trial.write()
        elif request == "sing":
            print("Cannot access audio at the moment")
        elif request == "speak":
            trial.speak()
        elif request == "battery":
            trial.battery_life()

