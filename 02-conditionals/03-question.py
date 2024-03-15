# Develop a code that reads 3 integers from user and decides
# which one is the largest
number_one = int(input("Enter the first number: "))
number_two = int(input("Enter the second number: "))
number_three = int(input("Enter the third number: "))

if number_one >= number_two and number_one >= number_three:
    print("The largest number is:", str(number_one))
elif number_two >= number_one and number_two >= number_three:
    print("The largest number is:", str(number_two))
else:
    print("The largest number is:", str(number_three))