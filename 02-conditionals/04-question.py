# Develop a program to that reads an integer of the number is even or odd
number = int(input("Enter a number"))
if number % 2 == 0:
    print(str(number) + " is an even number")
else:
    print(str(number)+ " is a odd number")