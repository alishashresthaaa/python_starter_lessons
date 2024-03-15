# Q3. Write a function named unique_elements that
# takes a list and returns a new list with only the
# unique elements from the original list.
# Example:
# print(unique_elements([1, 2, 2, 3, 4, 4]))
# # Output: [1, 2, 3, 4]

def unique_elements(user_list):
    unique_list = []
    for item in user_list:
        if item not in unique_list:
            unique_list.append(item)
    return  unique_list


print(unique_elements([1, 2, 2, 3, 4, 4]))