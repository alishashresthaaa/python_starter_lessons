# Exercise: Write a code that takes two strings, then it checks to see if first string is the part of second string
# For example: 'car' is part of 'racecar'
def match_string(first_string, second_string):
    if(first_string in second_string):
        print(first_string+ " is the part of " + second_string)
    else:
        print(first_string+ " is not the part of " + second_string)


match_string("car","racecar")
match_string("water","watermelon")
match_string("college","apartment")