#password length checker

password = str(input("Set Password: "))
if len(password) < 6:
    print("Try again!")
else:
    print("Set!")

