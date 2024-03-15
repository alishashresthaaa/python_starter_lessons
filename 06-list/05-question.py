# Exercise: provide code to see if word is palindrome
def is_palindrome(word):
    '''
    Loops through the string and checks if the letter is same from the start and the finish
    : param word:
    :return:
    '''
    for i in range(0, int(len(word))):
        if word[i] != word[len(word) - 1 - i]:
            print(word + " is not palindrome")
            return False

    print(word + " is palindrome")
    return True

user_input = input("Enter your word to check if its palindrome: ")
is_palindrome(user_input)