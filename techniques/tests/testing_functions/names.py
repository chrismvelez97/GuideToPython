                            # Input Name Program

'''
This is the program that will
prompt the user for his/her
name so we can run our format
name function on them.
'''

from name_functions import format_name as f

print ("Enter 'q' to quit at any time")
while True:
    first = input("Please enter a first name:\n")
    if first == 'q':
        break
    print()
    last = input("Please enter a last name:\n")
    if last == 'q':
        break
    print()
    full_name = f(first, last)
    print ("Neatly formatted name: {0}".format(full_name))
    break
