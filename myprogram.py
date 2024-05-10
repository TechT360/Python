Name = "Terry"
Acode ="2562"

user = input("Whats is the hostname = ")
if (user != Name):
    print("Unauthorised access!!!")
    quit
    
else:   
    print("Access Granted!!!")
    print("Moving to next sequence")

    print("Welcome to the next sequence now proceed with ACCESS CODE!")
    
    while True:
        code = input("Enter your Access Code : ")
        
        if code == Acode:
            print("Correct Access Code!!!")
            print("ACCESS GRANTED!!!")
            break
        else:
            print("Unauthorised access!!! try again")
print("wow nice one")  



   

