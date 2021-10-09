def gameplay():
    secret_word = input("player one please enter your secret word: ")
    for w in range(50):
        print(w*"")
    secret = "_"*len(secret_word)
    secret = list(secret)
    print("player 2 must guess Player one's word")
    current_progress = ""
    failed_guess = 0
    while current_progress != secret_word:
        guess = input("Player 2, please guess a letter: ")
        if guess in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    secret[i] = guess
            final = ""
            for x in secret:
                final += x
            print("current progress: ", final)
            if secret_word == final:
                print("you won!!!")
                break
        else:
            failed_guess += 1
            print("Your guess is incorrect, please try again!")
            print("Hangman status: ", end="")
            if failed_guess == 1:
                print("o")
            elif failed_guess == 2:
                print("o-")
            elif failed_guess == 3:
                print("o_o")
            elif failed_guess == 4:
                print("o-<")
            elif failed_guess == 5:
                print("o+<")
            elif failed_guess == 6:
                print("you died!!")
                break
            print("Number of chance left: ", 6-failed_guess)
            for p in range(2):
                print(p*"")
            if failed_guess == 6:
                print("You lost")
                break
    print("THANKS FOR PLAYING HANGMAN")

gameplay()