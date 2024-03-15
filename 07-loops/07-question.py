# Q2. Write a function named count_char that takes a
# string and a character, and counts how many times the
# character appears in the string
# Example:
# print(count_char("hello world", "o"))
# # Output: 2

def count_char(user_input, char):
    count_times = 0
    for i in range(0, int(len(user_input))):
        if user_input[i].lower() == char.lower():
            count_times += 1
    return count_times


get_count = count_char("hello world", "o")
print(get_count)