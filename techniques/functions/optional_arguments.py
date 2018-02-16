#                       How to use optional arguments

'''
As mentioned previously in arguments_parameters.py arguments can be optional in
code.

But how can we do this?  Most times when you don't include arguments you'll get
an error saying you're missing arguments.

So how do we bypass this?

To do this we use conditional statements and set the optional argument last
so that the positions of the arguments will be in the correct order.
'''


def get_formatted_name(first_name, last_name, middle_name=""):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


print (get_formatted_name("Christian", "Velez"))
