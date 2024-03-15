# The program reads an integer from user and prints the message if its positive, negative or zero

number = int(input("Enter an integer?"))
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")