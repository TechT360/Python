""""
Name: Terry.
Code ID:004.
Code type: Guessing game.
Date: 23|10|2024.

"""

import random

while True:
    name = input("Hi there, what shall I address you by: ")
    print("Pleased to know you,", name + "! Let's get started!")
    print("This is a number guessing game.")
    print("First, pick a MAX number you can guess up to.")
    print("Then, try to guess the random number.")
    print("The number of guesses will be shown when you get it right.")
    print("Have fun!")

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
        print("Thanks for playing", name, "have a great day!")
        break
    
    # End of project.
