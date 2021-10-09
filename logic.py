import pyfiglet
import termcolor
import random
import time
header = pyfiglet.figlet_format("*** LOGIC ***")
header = termcolor.colored(header, color="white", on_color="on_magenta", attrs=["concealed"])
print(header)
print("WELCOME TO THE WORLD OF THE GENIUSES... SOLVE ALL RIDDLES CORRECTLY TO BE CROWNED THE GRANDMASTER!!!")
score = 0
while score <= 40:
    if score in [5, 10, 15, 20, 25, 30, 35, 40]:
        proceed = input("Do you want to continue the game? (y/n) ")
        if proceed == "y":
            randint = random.randint(1, 70)
        elif proceed == "n":
            break
        else:
            print("insert either Y or N")
    randint = random.randint(1, 70)
    if randint == 1:
        riddle = input("what has to be broken before you can eat it? ").lower()
        if riddle == "egg":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is EGG...")
    elif randint == 2:
        riddle = input("i'm tall when i'm young, and i'm short when i'm old. what am i? ").lower()
        if riddle == "candle":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is CANDLE...")
    elif randint == 3:
        riddle = input("what month of the year has 28 days in it? ").lower()
        if riddle in ["all", "all of them"]:
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is ALL THE MONTHS...")
    elif randint == 4:
        riddle = input("what is full of holes but still holds water? ").lower()
        if riddle == "sponge" or riddle == "foam":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is SPONGE...")
    elif randint == 5:
        riddle = input("what question can you never say yes to? ").lower()
        if riddle == "are you sleeping yet":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is ARE YOU SLEEPING YET...")
    elif randint == 6:
        riddle = input("what is always in front of you but can't be seen? ").lower()
        if riddle == "future":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is FUTURE...")
    elif randint == 7:
        riddle = input("what can you keep after giving to someone? ").lower()
        if riddle == "word" or riddle == "words":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is WORDS...")
    elif randint == 8:
        riddle = input("what can you break even if you never pick it up or touch it? ").lower()
        if riddle == "promise":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is PROMISE...")
    elif randint == 9:
        riddle = input("what goes up but never comes down? ").lower()
        if riddle == "age":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is AGE...")
    elif randint == 10:
        riddle = input("i shave every day, but my beard still stays the same. What  am i? ").lower()
        if riddle in ["barber"]:
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is BARBER...")
    elif randint == 11:
        riddle = input("what get wet while drying? ").lower()
        if riddle == "towel":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is TOWEL...")
    elif randint == 12:
        riddle = input("you walk into a room that contains a match, a kerosene lamp, candle and a fireplace. "
                       "What would you light first? ").lower()
        if riddle == "match":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is MATCH...")
    elif randint == 13:
        riddle = input("i have branches, but no fruit, trunk or leaves. what  am i? ").lower()
        if riddle == "bank":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is BANK...")
    elif randint == 14:
        riddle = input("what can't talk but will reply when spoken to? ").lower()
        if riddle == "echo":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is ECHO...")
    elif randint == 15:
        riddle = input("the more of this there is, the less you see. what am i? ").lower()
        if riddle == "darkness":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is DARKNESS...")
    elif randint == 16:
        riddle = input("david's parents have three sons: snap, crackle, and what's the name of the third son? ").lower()
        if riddle == "david":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is DAVID...")
    elif randint == 17:
        riddle = input("i follow you all the time and copy your every move, but you can't stop me. What am i? ").lower()
        if riddle == "shadow":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is SHADOW...")
    elif randint == 18:
        riddle = input("what is black when it's clean and white when it's dirty? ").lower()
        if riddle == "chalkboard":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is CHALKBOARD...")
    elif randint == 19:
        riddle = input("what gets bigger when more is taken away? ").lower()
        if riddle == "hole":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is HOLE...")
    elif randint == 20:
        riddle = input("i'm light as a feather, yet the strongest person can't hold me for five minutes. what am i? ").lower()
        if riddle == "breath":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is BREATH...")
    elif randint == 21:
        riddle = input("i'm found in socks, scarves and mittens; and often in the paws of a playful kittens. "
                       "what am i? ").lower()
        if riddle == "yarn":
            print("CORRECT...")
        else:
            print(f"{riddle} is INCORRECT, the answer is YARN...")
    elif randint == 22:
        riddle = input("where does today come before yesterday? ").lower()
        if riddle == "dictionary":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is DICTIONARY...")
    elif randint == 23:
        riddle = input("what invention lets you look right through a walls? ").lower()
        if riddle == "window":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is WINDOW...")
    elif randint == 24:
        riddle = input("if you've got me, you want to share me; if you share me, you haven't kept me. what am i? ").lower()
        if riddle == "secret":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is SECRET...")
    elif randint == 25:
        riddle = input("what goes up and down but doesn't move? ").lower()
        if riddle in ["stairs", "staircase"]:
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is STAIRCASE...")
    elif randint == 26:
        riddle = input("it belongs to you, but other people use it more than you do. what is it? ").lower()
        if riddle in ["your name", "name"]:
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is YOUR NAME...")
    elif randint == 27:
        riddle = input("what has hands but can't clap? ").lower()
        if riddle == "clock":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is CLOCK...")
    elif randint == 28:
        riddle = input("what can you catch but not throw? ").lower()
        if riddle == "cold":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is COLD...")
    elif randint == 29:
        riddle = input("what has many teeth but can't bite? ").lower()
        if riddle == "comb":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is COMB...")
    elif randint == 30:
        riddle = input("what has words but can't speak? ").lower()
        if riddle == "book":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is BOOK...")
    elif randint == 31:
        riddle = input("what runs all around a backyard, yet never moves? ").lower()
        if riddle == "fence":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is FENCE...")
    elif randint == 32:
        riddle = input("what can travel all around the world without leaving its corner? ").lower()
        if riddle == "stamp":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is STAMP...")
    elif randint == 33:
        riddle = input("what has thumb and four fingers, but is not a hand? ").lower()
        if riddle == "glove":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is GLOVE...")
    elif randint == 34:
        riddle = input("what has a head and a tail but has no body? ").lower()
        if riddle == "coin":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is COIN...")
    elif randint == 35:
        riddle = input("where does one wall meet the other wall? ").lower()
        if riddle in ["corner", "on the corner", "in the corner", "corner of the walls", "at the corner"]:
            print("ON THE CORNER IS CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is ON THE CORNER...")
    elif randint == 36:
        riddle = input("what building has the most stories? ").lower()
        if riddle == "library":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is LIBRARY...")
    elif randint == 37:
        riddle = input("it stalks the countryside with ears that can't hear. What am i? ").lower()
        if riddle == "corn":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is CORN...")
    elif randint == 38:
        riddle = input("what has bottom at the top? ").lower()
        if riddle == "leg":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is LEG...")
    elif randint == 39:
        riddle = input("i am an odd number. Take away a letter and i become even. What am i? ").lower()
        if riddle == "seven":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is SEVEN...")
    elif randint == 40:
        riddle = input("if two is company, and three's a crowd, what are four and five? ").lower()
        if riddle == "nine":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is NINE...")
    elif randint == 41:
        riddle = input("Mary has four daughters,  and each of her daughter has a brother. "
                       "How many children does mary have? ").lower()
        if riddle == "five":
            print("CORRECT...")
            score += 1
            print("each daughter has the same brother")
        else:
            print(f"{riddle} is INCORRECT, the answer is FIVE...")
            print("each daughter has the same brother")

    elif randint == 42:
        riddle = input("which is heavier: a ton of bricks or a ton of feathers? ").lower()
        if riddle in ["neither", "none"]:
            print("CORRECT...")
            score += 1
            print("they both weigh a ton")
        else:
            print(f"{riddle} is INCORRECT, the answer is NEITHER...")
            print("they both weigh a ton")

    elif randint == 43:
        riddle = input("Three doctors said that Bill was their brother. Bill says he has no brothers. "
                       "How many brother does Bill actually have? ").lower()
        if riddle == "none":
            print("CORRECT...")
            score += 1
            print("he has three sisters")
        else:
            print(f"{riddle} is INCORRECT, the answer is NONE...")
            print("he has three sisters")

    elif randint == 44:
        riddle = input("a little girl goes to the store and buys dozen eggs. as she is going home, all but three break."
                       " How many eggs are left unbroken? ").lower()
        if riddle == "three":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is THREE...")
    elif randint == 45:
        riddle = input("A man describes his daughters saying, 'They are all blonde, but two; all brunette but two; "
                       "and all redheaded but two'. how many daughters does he have? ").lower()
        if riddle == "three":
            print("CORRECT...")
            score += 1
            print("a blonde, a brunette and a redheaded")
        else:
            print(f"{riddle} is INCORRECT, the answer is THREE...")
            print("a blonde, a brunette and a redheaded")

    elif randint == 46:
        riddle = input("if there are three apples and you take away two, how many apple do you have? ").lower()
        if riddle == "two":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is TWO...")
    elif randint == 47:
        riddle = input("what five-letter word becomes shorter when you add two letters to it? ").lower()
        if riddle == "short":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is SHORT...")
    elif randint == 48:
        riddle = input("what begins with 'e' and only contains one letter? ").lower()
        if riddle == "envelope":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is ENVELOPE...")
    elif randint == 49:
        riddle = input("a word i know, six letters it contains, remove one letter and 12 remains. What is it? ").lower()
        if riddle == "dozens":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is DOZENS...")
    elif randint == 50:
        riddle = input("what would you find in the middle of Toronto? ").lower()
        if riddle == "o":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is O...")
    elif randint == 51:
        riddle = input("you see me once in June, twice in November and not at all in may. What am i? ").lower()
        if riddle == "e":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is E...")
    elif randint == 52:
        riddle = input("two in a corner, one in a room, zero in a house, but one in a shelter. What is it? ").lower()
        if riddle == "r":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is R...")
    elif randint == 53:
        riddle = input("i am the beginning of everything, and the end of everywhere. I'm the beginning of eternity, "
                       "the end of time and space. What am i? ").lower()
        if riddle == "e":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is E...")
    elif randint == 54:
        riddle = input("i'm a word, when you read me backward i am heavy, but forward i am not. what am i? ").lower()
        if riddle == "not":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is NOT...")
    elif randint == 55:
        riddle = input("what is 3/7 chicken, 2/3 cat and 2/4 goat? ").lower()
        if riddle == "chicago":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is CHICAGO...")
    elif randint == 56:
        riddle = input("i'm a three-letter word, add two more and i become fewer. what am i? ").lower()
        if riddle == "few":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is FEW...")
    elif randint == 57:
        riddle = input("what word of five letters has one left when two are removed? ").lower()
        if riddle == "stone":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is STONE...")
    elif randint == 58:
        riddle = input("what is the end of everything? ").lower()
        if riddle == "g":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is G...")
    elif randint == 59:
        riddle = input("what word is pronounced the same it's first letter is also pronounced? ").lower()
        if riddle == "queue":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is QUEUE...")
    elif randint == 60:
        riddle = input("what word in the English language does the following: The first two letters signify a male,"
                       " the first three letter signify a female, the first four letter signify a great, "
                       "while the entire word signifies a great woman. What is the word? ").lower()
        if riddle == "heroine":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is HEROINE...")
    elif randint == 61:
        riddle = input("what is so fragile that saying it name breaks it? ").lower()
        if riddle == "silence":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is SILENCE...")
    elif randint == 62:
        riddle = input("what can fill a room but takes up no space? ").lower()
        if riddle == "light":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is LIGHT...")
    elif randint == 63:
        riddle = input("if you drop me i'm sure to crack, but give me a smile and i'll always smile back. What am i? ").lower()
        if riddle == "mirror":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is MIRROR...")
    elif randint == 64:
        riddle = input("the more you take the more you leave behind. what are they? ").lower()
        if riddle in ["footsteps", "footstep"]:
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is FOOTSTEP...")
    elif randint == 65:
        riddle = input("people make me, save me, change me, raise me. What am i? ").lower()
        if riddle == "money":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is MONEY...")
    elif randint == 66:
        riddle = input("what goes through cities and fields, but never moves? ").lower()
        if riddle == "road":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is ROAD...")
    elif randint == 67:
        riddle = input("i am always hungry and will die if not fed, but whatever i touch will soon turn red. "
                       "What am i? ").lower()
        if riddle == "fire":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is FIRE...")
    elif randint == 68:
        riddle = input("The person who makes it has no need of it; the person who buys it has no use for it. "
                       "The person who uses it can neither see nor feel it. What is it? ").lower()
        if riddle == "coffin":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is COFFIN...")
    elif randint == 69:
        riddle = input("with pointed fangs i sit and wait; with piercing force i crunch out fate; grabbing victims, "
                       "proclaiming might; physically joining with a single bite. What am i? ").lower()
        if riddle == "stapler":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is STAPLER...")
    else:
        riddle = input("i have lakes with no water, mountains with no stones and cities with no buildings. what am i? ").lower()
        if riddle == "map":
            print("CORRECT...")
            score += 1
        else:
            print(f"{riddle} is INCORRECT, the answer is MAP...")
    if score == 1:
        print("YOU ARE A GREAT GURU...")
    elif score == 11:
        print("WORLD GREATEST GENIUS...")
    elif score == 21:
        print("WORLD MOST GIFTED HUMAN...")
    elif score == 31:
        grandmaster = pyfiglet.figlet_format("\n***GRANDMASTER***\n")
        effect = termcolor.colored(grandmaster, color="white", on_color="on_blue", attrs=["blink"])
        print(effect)
        time.sleep(10)
        break
