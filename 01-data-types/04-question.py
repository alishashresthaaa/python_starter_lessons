# Question 2: Word Reversal
# Write a Python function reverse_words(sentence) that:
# Takes a sentence as input.
# Reverses the order of the words in the sentence.
# Returns the modified sentence.
# For example, reverse_words("Hello world") should return "world Hello".
def word_reversal(user_input):
    """
    Reverses the order of the words in the sentence.
    :param user_input:
    :return:
    """
    words_array = user_input.split()
    reversed_array = words_array[::-1]
    reversed_user_input = ' '.join(reversed_array)
    return reversed_user_input


user_input = input("Enter your sentence: ")
reversed_output = word_reversal(user_input)
print("Reversed output is: ", reversed_output)