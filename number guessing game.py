""""
Name: Terry.
Code ID:004.
Code type: Guessing game.
Date: 23|10|2024.

"""

import random
import time

while True:
    
    name = input("Hi there, what shall I address you by: ")

    intro_text = (
        "Pleased to know you, " + name + "!\n"
        "Let's get started!\n"
        "This is a number guessing game.\n"
        "First, pick a MAX number you can guess up to.\n"
        "Then, try to guess the random number.\n"
        "The number of guesses will be shown when you get it right.\n"
        "Have fun!\n"
    )

    for char in intro_text:
        print(char, end='', flush=True)
        time.sleep(0.1)
    time.sleep(3)
    


    top_of_range = input("Enter a number: ")

    if top_of_range.isdigit():
        top_of_range = int(top_of_range)

        if top_of_range <= 0:
            print("Please input a number larger than 0 next time.")
            quit()
    else:
        print("Please type a number next time.")
        quit()

    random_number = random.randint(0, top_of_range)
    guesses = 0

    while True:
        guesses += 1
        user_guess = input("Make a guess: ")

        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            print("Please type a number next time.")
            continue

        if user_guess == random_number:
            print("You got it right!")
            break
        elif user_guess > random_number:
            print(name + ", you were above the number!")
        else:
            print(name + ", you were below the number!")

    print(name, "you had", guesses, "guesses.")

    play_again = input("Do you want to play again? (yes/no): ")
    
    if play_again.lower() != 'yes':
        Thanks = ("Thanks for playing " + name + " have a great day!\n")
        
        for char in Thanks:
            print(char, end='', flush=True)
            time.sleep(0.1)
        for char in name:
            print(char, end='', flush=True)
            time.sleep(0.1)
        break
    
    # End of project.
