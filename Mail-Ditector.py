
mail = str(input("Enter mail: "))
if "@northsouth.edu" in mail:
    print("NSU Mail!")
elif "@iub.edu.bd" in mail:
    print("IUB Mail!")
elif "@gmail.com" in mail:
    print("Google Mail!")
elif "@yahoo.com" in mail:
    print("Yahoo Mail!")
else:
    print("Cannot detect!")