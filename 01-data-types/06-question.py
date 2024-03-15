# Question 4: Substring Occurrences
# Write a Python function count_substring(string, sub_string) that:
# Takes two strings as input: string and sub_string.
# Returns the number of times sub_string occurs in string, including overlaps.
# For example, count_substring("ABCDCDC", "CDC") should return 2.

def count_substring(string, substring):
    '''

    :param string:
    :param substring:
    :return:
    '''
    count = 0
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            count +=1

    return count


user_input_string = "ABCDCDC"
sub_string = "CDC"
output_count = count_substring(user_input_string, sub_string)
print("Number of occurance of ", sub_string, " in ", user_input_string, " is ", output_count)

