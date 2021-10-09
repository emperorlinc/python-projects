club = input("what's your age ")
if club != "":
    club = int(club)
    if club < 18:
        print("you're too young to party")
    elif 18 <= club < 21:
        print("you can go in, but too young you to have an alcohol")
    elif club >= 21:
        print("go in and have fun")
else:
    print("insert your age")
