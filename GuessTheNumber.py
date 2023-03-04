import random

def guessTheNumber(prompts, lLimit, uLimit):
    number = random.randint(lLimit,uLimit)
    guess = int(input("Guess the number: "))
    guesses = 0

    while guess != number:
        guesses+=1
        if number > guess:
            print("Sorry, too low")
        else:
            print("Sorry, too high")
        if guesses%prompts == 0:
            quit = input("Give up (y/n)? ")
            if quit == "y" or quit == "yes":
                print("Aw. You made {} attempts. The number was {}.".format(guesses, number))
                break
        guess = int(input("Guess the number: "))
    if number == guess:
        print("""Correct! Congratulations :)
    number: {}
    guesses: {}""".format(number, guesses))
    print()
    check = input("Return to menu (y/n)? ")
    if check == "y" or check == "yes":
        print()
        print("loading...")
        print()
        menu()
    else:
        print("Thank you for playing.")
        
def rules():
    print("""
    The computer will decide on a number between the limits you set in the game.
    If you guess too high or low, the computer will tell you.
    If you are right, you win!
    You set a prompt counter that asks if you would like to give up every *prompt counter* number of turns.
    If you say yes, your number of guesses and the answer will be returned and your score will be DNF (not recorded on scoreboard).

    """)
    check = input("Return to menu (y/n)? ")
    while check != "y" and check != "yes":
        check = input("Return to menu (y/n)? ")
    print()
    print("loading...")
    print()
    menu()

def scoreboard(guesses = 0, number = 0, guess = 0):
    if guesses == 0 and number == 0 and guess == 0:
        print("Scoreboard currently empty. Play then come back!")
        print()
        menu()
    else:
        scores = {}
        user = input("Enter player name: ")
        with open("scores.txt", "w") as file:
            if number == guess:
                file.write("{},{}".format(user, guesses))
        with open("scores.txt", "r") as file:
            for line in file.readlines():
                l = line.strip.split(",")
                scores[l[0]] = scores[l[1]]         
            if guess == number:
                scores[user] = guesses
            values = scores.values()
            values.sort(reverse=True)
            print("*"*16+"SCOREBOARD"+"*"*16)
            i = 0
            for value in values:
                i+=1
                user = [u for u in scores if scores[u] == value]
                print("{}. {}: {}".format(i, user[0], value))
            print("*"*60)
        while check != "y" or check != "yes":
            check = input("Return to menu (y/n)? ")
        menu()

def menu():
    print("*"*16 + "WELCOME TO GUESS THE NUMBER"+"*"*16)
    print("""1. Play
2. Rules
3. Scoreboard
4. Quit""")
    print("*"*60)
    select = int(input("Select an option(1-4): "))
    if select == 1:
        prompts = int(input("I would like a give up prompt every ... attempts: "))
        lLimit = int(input("minimum number: "))
        uLimit = int(input("maximum number: "))
        print()
        print("loading...")
        print()
        print("Start!")
        guessTheNumber(prompts, lLimit, uLimit)
    if select == 2:
        rules()
    if select == 3:
        scoreboard()
    if select == 4:
        check = input("Are you sure (y/n)? ")
        if check == "y" or "yes":
            print("Thank you for playing.")
        else:
            menu()

menu()