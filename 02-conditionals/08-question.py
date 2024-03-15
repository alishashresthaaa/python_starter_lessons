# Question
# 1: Conditionals(40 Points)
# In a fictional world, there's a peculiar clock that operates differently
# from the clocks we are used to. This clock has a unique way of displaying time based
# on the day of the week and specific conditions related to environmental factors.
# Your task is to simulate this clock' s behavior using Python, focusing on conditional statements.
# Problem Statement
# Write a Python program that simulates the behavior of this peculiar clock.The clock displays time based on the following rules:
# Standard
# Mode: On
# Mondays, Tuesdays, and Wednesdays, the
# clock
# operates
# normally, displaying
# the
# current
# time in a
# 24 - hour
# format(HH: MM).
#
# Reverse
# Mode: On
# Thursdays, the
# clock
# runs in reverse.For
# every
# hour
# that
# passes, the
# clock
# subtracts
# an
# hour
# from the display.For
# example,
# if the actual time is 15:00, the
# clock
# displays
# 0
# 9: 00(24 - 15 = 9).Minutes
# are
# displayed
# normally.
#
# Double
# Mode: On
# Fridays, the
# clock
# moves
# twice as fast.If
# the
# actual
# time is 14: 30, the
# clock
# displays
# 05: 00(14 * 2 = 28, but
# since
# we
# 're using a 24-hour format, 28 - 24 = 4, and 30 minutes remain the same).
#
# Static
# Mode: On
# Saturdays and Sundays, the
# clock
# displays
# a
# static
# time
# based
# on
# environmental
# conditions:
# If
# it
# 's sunny, the clock displays 12:00, regardless of the actual time.
# If
# it
# 's rainy, the clock displays 18:30, regardless of the actual time.
# In
# any
# other
# condition, the
# clock
# displays
# 00: 00.
#
# Your
# program
# should:
# •    Accept
# two
# inputs: the
# day
# of
# the
# week( as a
# string) and the
# current
# time( in 24 - hour
# format
# HH: MM).
# •    Accept
# an
# additional
# input
# for Saturdays and Sundays that specifies the environmental condition (sunny, rainy, or other).
# •    Output the time as displayed by the peculiar clock based on the rules described above.
#
# Example Input and Output
# Input: Monday, 13: 45
# Output: 13:45
# Input: Thursday, 16: 20
# Output: 0
# 8: 20
# Input: Friday, 11: 15
# Output: 22:15
# Input: Sunday, anytime, sunny
# Output: 12:00
#
# Constraints
# •    Assume
# the
# input
# time is always
# valid.
# •    The
# day
# of
# the
# week is case - insensitive(e.g., "monday", "Monday", and "MONDAY"
# are
# treated
# the
# same).
# For
# simplicity, ignore
# daylight
# saving
# time
# adjustments and leap
# seconds.


def modifying_datetime(input_day, input_time, input_condition=None):
    hours = int(input_time.split(":")[0]) if input_time != "anytime" else 0
    minutes = int(input_time.split(":")[1]) if input_time != "anytime" else 0

    if input_day.lower() == "monday" or input_day.lower() == "tuesday" or input_day.lower() == "wednesday":
        return "{:02d}:{:02d}".format(hours, minutes)
    elif input_day.lower() == "thursday":
        reversed_hours = 24 - hours
        return "{:02d}:{:02d}".format(reversed_hours, minutes)
    elif input_day.lower() == "friday":
        double_hours = (hours * 2) % 24
        return "{:02d}:{:02d}".format(double_hours, minutes)
    elif input_day.lower() == "saturday" or input_day.lower() == "sunday":
        if input_condition == "sunny":
            return "12:00"
        elif input_condition == "rainy":
            return "18:30"
        else:
            return "00:00"


print(modifying_datetime("Monday", "13:45"))
print(modifying_datetime("Thursday", "16:20"))
print(modifying_datetime("Friday", "11:15"))
print(modifying_datetime("Sunday", "anytime", "sunny"))