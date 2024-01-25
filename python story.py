
names = ["John", "Mark", "Peter"]
print("There 3 names in an array that starts with the letter J, M and P.")
print("you are to guess one of them.")

while True:
    user = input("Guess a name: ")

    if user.lower() in [name.lower() for name in names]:
        print(user + ", Well done.")
    else:
        print(user + ", is wrong.")
        
    play_again = input("Do you want to guess again? (yes/no): ")
    
    if play_again.lower() != 'yes':
        break  # Exit the loop if the user doesn't want to play again
