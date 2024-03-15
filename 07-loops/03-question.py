# 3-	Write a Python program to get a string from a given string
# where all occurrences of its first char have been changed to '$', except the first char itself
# Sample String : 'restart'
# Expected Result : 'resta$t'
def replace_first_char(word, replacement = '$'):
    first_char = word[0]
    new_word = first_char
    for ch in word[1:]:
        if ch.lower() == first_char.lower():
            new_word += replacement
        else:
            new_word += ch
    return new_word


user_input = input("Enter string: ")
print(replace_first_char(user_input))