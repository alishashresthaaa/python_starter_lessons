# 2-	 Write a Python program to count the number of characters (character frequency) in a string
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
def get_counts(word):
    output = {}
    for ch in word:
        if ch in output:
            output[ch] += 1
        else:
            output[ch] = 1
    return output


user_input = input("Enter string: ")
print(get_counts(user_input))
