# 1-	Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.
from calendar import month
given_year = int(input("Enter the year: "))
given_month = int(input("Enter the month in number: "))
generated_calendar = month(given_year, given_month)
print("Your calendar is \n" + generated_calendar)
