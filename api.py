import requests
import pickle
from pyfiglet import figlet_format
from termcolor import colored

content = figlet_format("Always Remember This, It's You Before Anyone")
display = colored(content, color="cyan", on_color="on_magenta", attrs=['blink'])


def unpickle():
    with open("login.pickle", "rb") as file:
        retrieve = pickle.load(file)
        return retrieve


class CreateAccount:

    def navigation(self):
        print("You can simply change your password by inputting RESET PASSWORD")
        search = input("navigation bar: ").lower()
        if search == "login":
            unpickle()
            return x.login()
        return search

    def login(self):
        username = input("username: ").lower()
        password = input("password: ").lower()
        if username not in unpickle():
            print("incorrect username")
        elif password not in unpickle():
            print("incorrect password")
        else:
            print(display)


x = CreateAccount()
x.navigation()
