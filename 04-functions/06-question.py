# 5-	Write a Python function that takes a list of words and return the longest word and the length of the longest one.
# Sample Output:
# Longest word: Exercises, Hockey
# Length of the longest word: 9

def get_longest_word(list):
    length_of_longest_word = len(list[0])
    longest_word = list[0]
    for word in list:
        if len(word) > length_of_longest_word:
            length_of_longest_word = len(word)
            longest_word = word
    return longest_word, length_of_longest_word


words = ["Exercises", "Hockey", "Yoga"]
longest_word, length = get_longest_word(words)
print("Longest word:", longest_word)
print("Length of the longest word:", length)