# Write a Python program that converts a list of
# integers into a list of strings.
# Use a loop to iterate through the list and convert
# each integer to a string. For example, [1, 2, 3]
# should be converted to ["1", "2", "3"].

def int_to_string(user_input_list):
    '''
    Coverts the input items in array to strings
    :param user_input_list:
    :return:
    '''
    string_array = []
    for i in user_input_list:
        string_array.append(str(i))
    return string_array


user_list = [1, 2, 3]
print(int_to_string(user_list))

