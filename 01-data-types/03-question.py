# Question 1: String Basics
# Write a Python program that asks the user
# to enter their full name (including any middle names). The program should then:
# Print the name in uppercase.
# Print the total number of characters in the name, excluding spaces.
# Print the initials of the name.

user_full_name = input("Enter your full name: ")
uppercase_full_name = user_full_name.upper()
total_characters = len(user_full_name.replace(" ", ""))
user_name_array = user_full_name.split(" ")
user_name_initials = ''.join([i[0].upper() for i in user_name_array])
print("Name in uppercase: ", uppercase_full_name)
print("Total characters in name excluding space: ", total_characters)
print("User Initials: ", user_name_initials)

