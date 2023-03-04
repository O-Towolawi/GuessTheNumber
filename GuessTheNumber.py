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

def menu():
    print("*"*16 + "WELCOME TO GUESS THE NUMBER"+"*"*16)
    print("""1. Play
2. Rules
3. Quit""")
    print("*"*60)
    select = int(input("Select an option(1-3): "))
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
        check = input("Are you sure (y/n)? ")
        if check == "y" or "yes":
            print("Thank you for playing.")
        else:
            menu()

menu()