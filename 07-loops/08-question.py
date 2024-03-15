# Q4. Write a function to find all prime factors of a number.
import math

def get_prime_factors(user_input):
    factors_list = []
    while user_input % 2 == 0:
        factors_list.append(2)
        user_input = user_input // 2

    for i in range(3, int(math.sqrt(user_input)) + 1, 2):
        while user_input % i == 0:
            factors_list.append(i)
            user_input = user_input // i

    if user_input > 2:
        factors_list.append(user_input)

    return factors_list


print(get_prime_factors(120))