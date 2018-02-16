                # Functions to be used throughout the test folder

# Passing function
# def format_name(first, last):
#     '''Generates a fully formatted name, given a first and last name'''
#     full_name = first + " " + last
#     return full_name.title()

# print (format_name('janis', 'joplin'))

# Failing function
# def format_name(first, middle, last):
#     '''Generates a neatly formatted name'''
#     full_name = first + " " + middle + " " + last
#     return full_name.title()

# Passing function with multiple tests
def format_name(first, last, middle = ""):
    '''Generates a neatly formatted name'''
    if middle:
        full_name = first + " " + middle + " " + last
    else:
        full_name = first + " " + last
    return full_name.title()
