# Name: Terry Agabi
import string, secrets

chrs = string.ascii_letters 
numbers = string.digits

choose = input("Password or pin? ")
if choose == "password":
    length = input("Choose your password length: ")
elif choose == "pin":
    length = input("Choose your pin length: ")
else:
    print("Invalid choice.")
    exit()

password_in_chrs = ''.join(secrets.choice(chrs + numbers) for i in range(int(length)))
password_in_numbers = ''.join(secrets.choice(numbers) for i in range(int(length)))

if choose == "password":
    print(password_in_chrs)
    
if choose == "pin":
    print(password_in_numbers)
print("**********Python Password Generator**********")
