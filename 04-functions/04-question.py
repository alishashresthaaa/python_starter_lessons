# 3- Write a Python program find a list of integers with exactly two occurrences
# of nineteen and at least three occurrences of five.
def check_array(arr):
    has_nineteen = 0
    has_five = 0
    for i in range(0, len(arr)):
        if arr[i] == 19:
            has_nineteen += 1
        if arr[i] == 5:
            has_five += 1
    if has_nineteen == 2 and has_five >= 3:
        return True
    else:
        return False


print(check_array([19, 19, 15, 5, 3, 5, 5, 2]))
print(check_array([19, 15, 15, 5, 3, 3, 5, 2]))
print(check_array([19, 19, 5, 5, 5, 5, 5]))