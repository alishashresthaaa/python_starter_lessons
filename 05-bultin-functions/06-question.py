# 2-Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days
# from datetime import date

def difference_in_date(first_date, last_date):
    '''
    Difference between dates using datetime module > *last_date is unpacking the tuple
    :param first_date:
    :param last_date:
    :return:
    '''
    difference = date(*last_date) - date(*first_date)
    print("The difference between " + str(first_date) + " and " + str(last_date) + " is " + str(
        abs(difference.days)) + " days.")


first_date = (2014, 7, 2)
last_date = (2014, 7, 11)
difference_in_date(first_date, last_date)