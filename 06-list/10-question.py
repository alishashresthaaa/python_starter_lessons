# Write a Python program that uses list comprehension
# to create a list of squares
# for all even numbers between 1 and 20, inclusive.
# Print the final list.

def get_squared_numbers(start, end):
    '''
    Returns squared numbers from the given range inclusive
    :param start:
    :param end:
    :return:
    '''

    for n in range (start, end + 1):
        if n % 2 == 0:
            print(n ** 2)


get_squared_numbers(1, 20)

