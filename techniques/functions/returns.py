#                           What is a return?

'''
So far, most of this code has been about displaying information but in order
for the computer to use the information a function process, you will have to
use return.

This allows us to use code from a function for something else.
'''


def get_formatted_name(first_name, last_name):
    # Returns a full name neatly formatted
    full_name = first_name + " " + last_name
    return full_name.title()


#   Note how if we execute this code it doesn't display anything
get_formatted_name("jimi", "hendricks")

#   If we wanted to display what gets outputted we can print the function
print (get_formatted_name("jimi", "hendricks"))
