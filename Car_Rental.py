print("=========================")
print("Available Car Types")
print("1. Hatchback")
print("2. Sedan")
print("3. SUV")
print("=========================")

userChoice1 = input("Enter Car Type Name: ")
userChoice2 = int(input("How many days you would like to borrow this Car:"))
if userChoice1 == "Hatchback":
    print("you have choose Hatchback car type")
    print("Rent of will be $30 *", userChoice2)
elif userChoice1 == "Sedan":
    print("you have choose Sedan car type")
    print("Rent of will be $50 *", userChoice2)
elif  userChoice1 == "SUV":
    print("you have choose Sedan car type")
    print("Rent of will be $100 *", userChoice2)
else:
    print("Enter car name only from the list")
