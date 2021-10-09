# hints and clues will be provided,  use the hints to guess the write word
from pyfiglet import figlet_format as font
from termcolor import colored


def customize():
    name = input("what do you want to customize: ")
    term = font(name)
    term = colored(term, color="magenta", on_color="on_white")
    return term
customize()