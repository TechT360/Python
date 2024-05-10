# The Fride

user = input("Enter the fridge temperature : ")

user = float(user)
if user < 0:
    print (" Fridge too cold.")
elif user in range(5):
    print("Fridge OK.")
elif user in range(4, 7):
    print("Fridge too warm.")
else:
    print("Fridge broken.")
  
