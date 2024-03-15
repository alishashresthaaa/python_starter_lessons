# Question 3: Lists and List Comprehensions (20 Points)
# Scenario: You are working on a Python script that processes a list of temperatures in Celsius and converts them to Fahrenheit. Given a list of temperatures in Celsius: [30, 78, 41, 80]
# Use a list comprehension to convert each temperature to Fahrenheit. The formula to convert Celsius to Fahrenheit is (C * 9/5) + 32.
# Print the resulting list of temperatures in Fahrenheit.


def convert_tempertaure(celsius_list):
    fahrenheit_list = []
    for item in celsius_list:
            item = (item * 9/5) + 32
            fahrenheit_list.append(item)
    return fahrenheit_list


celsius_list = [42, 12, 56]
print("The converted temperature in fahrenheit is: ",convert_tempertaure(celsius_list))
