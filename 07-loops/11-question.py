# Question 1: Looping Through Numbers (For Loops)
# Write a Python program that prints all the even numbers from
# 1 to 100, inclusive. Use a for loop to iterate through this range
# and the if statement to check for even numbers.

def get_even_numbers(start, end):
    '''
    Getting the even numbers from the given range inclusive
    :param start:
    :param end:
    :return:
    '''
    for n in range(start, end + 1):
        if n % 2 == 0:
            print(n)


get_even_numbers(1, 100)

