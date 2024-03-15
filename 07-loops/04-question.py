# # 1-Write a Python program to calculate the length of a string
def calculate_length(word):
    length = 0
    for char in word:
        length += 1
    return length


user_input = input("Enter string: ")
print(calculate_length(user_input))