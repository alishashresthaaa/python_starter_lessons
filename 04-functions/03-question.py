# 2-	Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
# Sample value of n is 5
# Expected Result : 615

def format_numbers(number):
    """
    For number n, it returns n+nn+nnn where n is concatenated
    :param number:
    :return:
    """
    return number + int(str(number) * 2) + int(str(number) * 3)


user_input = int(input("Enter a number: "))
formatted_number = format_numbers(user_input)
print("Result: ", formatted_number)