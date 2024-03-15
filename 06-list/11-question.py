# Question 4: Merge and Sort Lists (Lists and Sorting)
# Write a Python function merge_and_sort(list1, list2)
# that takes two lists of numbers as input,
# merges them into a single list, and
# then sorts the merged list in ascending order.
# The function should return the sorted list.

def merge_and_sort_list(list_one, list_two):
    '''
    Returns merge and sort the list
    :param list_one:
    :param list_two:
    :return:
    '''

    merged_list = list_one + list_two
    sorted_list = sorted(merged_list)
    return sorted_list


user_list_one = [3, 5, 1, 6]
user_list_two = [2, 4, 9, 7]
merged_and_sorted_output = merge_and_sort_list(user_list_one, user_list_two)
print(merged_and_sorted_output)


