# ====SECONDARY VERSION====
# from random import choice
# from time import sleep
# make a variable that consist of list of str sentences
# make the random.choice choose any sentence in a for loop
# make the loop sleep with the time module
# variable User input()
# conditional statement to check if random == User
# print accuracy after 5 sentences
from random import choice
import time
sentences = ["survival and success are two mutually exclusive element to life",
             "stars don't even try to shine, they just do it",
             "the best way to predict the future is to create it",
             "a friend of mine use to say that a man today is a man tomorrow",
             "life begins at the end of your comfort zone",
             "your fate may be set in stone, but how you live isn't",
             "We all don't even know who we are yet, we're just figuring that out as days pass by... "
             "The best we can do is just to reflect on who we are in the past and compare that to who we wanna "
             "be in the future and then spilt the difference. That who we are now",
             "everyone is going to be successful one way or the other on their different level, "
             "just that your testimony may not be as graceful as mine",
             "Look the wrong way and seasons turn, our lives are short but sorrows long. "
             "And so, we might as well just focus on the good stuff",
             "Truly to every dark tunnel, there's always a light at the end. And He that has promised to come "
             "will surely come through, He would not tarry and your testimony will be full",
             "We can always make back the money wasted, but we can't make back the time",
             "art of war is fighting the enemy where they are not",
             "why do we die to live since we live to die",
             "people that struggle the most and make it the hardest are gonna succeed, believe me!",
             "sometimes you fight, sometimes you be clever",
             "a sanctuary sometimes resides in the eye of the storm",
             "our worst day could be a blessing in disguise",
             "keep your friends close, but keep your enemies closer",
             "remember the promise of God is always true",
             "when a man's fortune is greater than his talent, then he is a superior man",
             "if you believe you are going to lose, then you have already lost",
             "i swear by The One, after night comes day and when your day comes, you will testify too that He is the Most Gracious, Most Merciful",
             "just because i'm a little weird doesn't make me less human, in fact it makes me more human",
             "don't just rely on external factors for your happiness, waiting for people to accept you instead of "
             "accepting yourself, i mean nothing can actually or possibly go wrong in accepting yourself for "
             "who you are"]


while True:
    baron = choice(sentences)
    print(baron)
    time_start = time.time()
    user = input()
    total_time = time.time() - time_start
    # individual_words = baron.spilt(" ")

    speed = round(total_time, 2)
    print(f"your speed = {speed}")
    if len(baron) == len(user) and baron == user:
        print("ACCURATE\n")
    elif len(baron) != len(user) and baron != user:
        print("GOOD JOB, TRY HARDER\n")
    else:
        print("try again\n")
