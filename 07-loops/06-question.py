# Q1. Write a function named sum_of_evens that
# takes a list of integers and returns the sum of
# only the even numbers.

def sum_of_events(input_list):
    sum_of_even = 0
    for number in input_list:
        if number % 2 == 0:
            sum_of_even += number
    return sum_of_even


get_sum = sum_of_events([1, 2, 3, 4, 5])
print("The sum of even numbers in the list is: " + str(get_sum))