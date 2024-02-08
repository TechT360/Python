import random

user_wins = 9
computer_wins = 0
options = ["rock", "paper", "scissors"] # this is a list

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit.").lower()
    if user_input == "q":
       break
        
    if user_input not in options :
        print("Invalid entry. Please type Rock, Paper, or Scissors.")
        continue
    
    random_number = random.randint(0, 2)
    # rock:0, paper:1, scissors:2
    computer_guess = options[random_number]
    print("Computer picked", computer_guess + ".")
    
    if user_input == "rock" and  computer_guess == "scissor":
        print("You won!")
        user_wins += 1
        
    elif user_input == "paper" and  computer_guess == "rock":
        print("You won!")
        user_wins += 1
       
    elif user_input == "scissors" and  computer_guess == "paper":
        print("You won!")
        user_wins += 1
        
    elif computer_guess ==  user_input:
        print("it's a draw")
        
    else:
        print("You lost!")
        computer_wins += 1
            
print("You won", user_wins, "times")
print("The computer won", computer_wins, "times")  
print("Goodbye!")   