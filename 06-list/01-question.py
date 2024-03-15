# Write a python program which accepts a squence of comma-seperated
# numbers from user and generate a list and a tuple with those numbers
user_numbers = input("Enter your numbers: ")
list = user_numbers.split(",")
tuple = tuple(list)
print('The list is:', list)
print('The tuple is:', tuple)
