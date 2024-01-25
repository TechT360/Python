print("Welcome to my computer quiz")
name = input("What is your name: ")

play = input(name + " do you want to play? ")

if play.lower() != "yes":
    quit()
    
print("let's play")
score = 0

question = input("What color is the sky? ")
if question.lower() == "blue":
    print("correct!")
    score += 1
    
else:
    print("incorrect, it is blue.")
 
    
question = input("What is the name The Rock? ")
if question.lower() == "Dwayne Johnson":
    print("correct!")
    score += 1
    
else:
    print("incorrect, it is Dwayne Johnson.")
    

question = input("What burns and its extremely hot? ")
if question.lower() == "fire":
    print("correct!")
    score += 1
    
else:
    print("incorrect, it is fire.")
    
    
question = input("What is used to open a lock? ")
if question.lower() == "key":
    print("correct!")
    score += 1
    
else:
    print("incorrect, it is key.")
    
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")