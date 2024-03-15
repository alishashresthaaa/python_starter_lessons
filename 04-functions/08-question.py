# Helper function inside a function > For privacy, encapsulation#
# The range from which the variable is defined is called scope

# This is a global function, that can be accessed throughout the program

# Can call the function that is defined after wards, as python saves it in the memory
def testFunction(x):
    return isPrime(x)


def isPrime(n):
    # The scope of this inner function is up to the outer function only
    # Called local variables. Defined and called with in the body of the function
    def isEven(x):
        return x%2 == 0

    if isEven(n):
        return False
    else:
        for i in range(3,n):
            if n%i == 0:
                return False
        return True


print(isPrime(5))
print(testFunction(5))