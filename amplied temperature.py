# The Fride

user = input("Enter the fridge temperature : ")

STATUS_COLD = " Fridge too cold."
STATUS_OK = "Fridge OK."
STATUS_WARM = "Fridge too warm."
STATUS_BROKEN = "Fridge broken."

status = STATUS_BROKEN      # there wont be a need to set an else statement for when the fridge is broken since default status is STATUS_BROKEN.


user = float(user)
if user < 0:
    status = STATUS_COLD
elif user in range(5):
    status = STATUS_OK
elif user in range(4, 7):
    status = STATUS_WARM

print(status)

