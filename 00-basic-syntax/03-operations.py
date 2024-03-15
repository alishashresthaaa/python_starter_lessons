# For paranthesis - first priority is given to the operation inside them
# if its neseted parathesis, the inner one gets executed first
expr_four = (26 - 3) * 2
# print(expr_four)
expr_five = ((26 - 3) + 3) + 2
# print(expr_five)

# EXERCISE
# create three expressions each having 5 operators
exe_one = 4 / 2 + 4 * 2 - 1 + 6
print("4 / 2 + 4 * 2 - 1 + 6: ", exe_one)
# 2 + 8 - 1 + 6
# 10 - 1 + 6
# 9 + 6
# 15

exe_two = 3 * ((6 / 2) - 1) * 3 + 1
print("3 * ((6 / 2) - 1) * 3 + 1: ",exe_two)
#  3 * (3 - 1) * 3 + 1
#  3 * 2 * 3 + 1
# 18 + 1
# 19

exe_three = 5 / 5 + 2 - ((1 * 2) + 2)
print("5 / 5 + 2 - ((1 * 2) + 2): ",exe_three)
# 5 / 5 + 2 - (2 + 2)
# 5 / 5 + 2 - 4
# 1 + 2 - 4
# 3 - 4
# -1