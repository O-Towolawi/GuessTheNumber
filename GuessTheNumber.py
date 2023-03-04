import random

prompts = int(input("I would like a give up prompt every ... attempts: "))
lLimit = int(input("minimum number: "))
uLimit = int(input("maximum number: "))

def guess(prompts, lLimit, uLimit):
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

guess(prompts, lLimit, uLimit)