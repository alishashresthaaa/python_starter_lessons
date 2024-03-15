# 1-Write a Python program to display the examination schedule. (extract the date from exam_st_date)
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

def format_date(date, seperator="/"):
    """
    This function converts the tuple in string with seperator
    :param date:
    :param seperator:
    :return:
    """
    return seperator.join(map(str, date))


exam_st_date = (11, 12, 2014)
output_date = format_date(exam_st_date, "/")

print("The examination will start from: ", output_date)