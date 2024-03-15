# Define a function that takes n and prints out the sum of all the prime numbers between 1 and n
# Note: 2 is not a prime number

def isPrime(number):
    if(number < 2): return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def sumOfPrimes(n):
    """
        @:param number
        @:return number
        This function returns the sum of primes
    """
    sum = 0
    for number in range(1, n +1):
        if isPrime(number):
            sum += number
    return sum


user_input = int(input("Enter a random number"))
result = sumOfPrimes(user_input)
print(f"The sum of {user_input} numbers is {result}")

