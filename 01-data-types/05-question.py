# Question 3: String Formatter
# Write a Python program that formats text strings for a simple text-based user interface. Given a string and a maximum line width, the program should:
# Wrap the text so that no line is longer than the maximum width.
# Justify the text to align both left and right sides by adding extra spaces between words as needed.
# Assume words in the input string are separated by a single space and that the input does not contain any newline characters.
# If a single word is longer than the maximum width, it does not need to be split.

import textwrap
def text_formatter(user_input_string, max_width):
    '''
    Returns wrapped text into the given max width
    :param user_input_string:
    :param max_width:
    :return:
    '''
    wrapped_string = textwrap.fill(user_input_string, max_width)
    formatted_text = textwrap.indent(wrapped_string, ' ' * (max_width - len(wrapped_string)))

    return formatted_text


user_input = "This is canada and it is winter season during the December and its too cold"
max_width = 22
user_formatted_text = text_formatter(user_input, max_width)
print(user_formatted_text)

