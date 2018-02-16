#                           How to use for if statements

'''
If statements are used to examine conditionals.  They can be used to check
a variety of things and depending on the outcome you can divert which way the
code runs.
'''
list = list(range(1, 11))
for item in list:
    if item % 2 == 1:  # This code just checks if our number (item) is odd.
        # The format() function allows us to insert variables into the string
        print ("The number {0} odd".format(item))
    else:
        # The format() function allows us to insert variables into the string
        print ("The number {0} even".format(item))

'''
The result of the code above is:

The number 1 odd
The number 2 even
The number 3 odd
The number 4 even
The number 5 odd
The number 6 even
The number 7 odd
The number 8 even
The number 9 odd
The number 10 even
'''
