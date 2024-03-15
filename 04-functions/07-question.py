# 4-	Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

def swap_string(string1, string2):
    output1 = string2[:2] + string1[2:]
    output2 = string1[:2] + string2[2:]

    return output1 + ' ' + output2


print(swap_string('abc', 'xyz'))