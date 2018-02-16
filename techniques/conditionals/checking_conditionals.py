#                           How to check conditionals

#   Checking for equality
print (1 == 1)
#   results: True

print (1 == 0)
#   results: False
#   While checking equalities you must use double equal sign

#   Checking for inequalities
print (1 != 1)
#   results: False
#   Even though 1 IS EQUAL to 1, the != symbol checks to see if it IS NOT EQUAL

print (1 != 0)
#   results: True
#   This basically means it is TRUE that 1  IS NOT EQUAL to 0

#   Checking for multiple conditionals
age = 5

'''
The following checks to see if age is less than five and greater than 5
which it is not. Note that the <, and > symbol does not include 5. To have
an inclusive check you must use <=, or >=
'''

print (age < 5 and age > 5)
#   results: False

'''
The following checks to see if age is odd AND if it is greater than 1 which it
is.  To check just one of the conditionals you can use the OR operators.
'''

print (age % 2 != 0 and age > 1)
#   results: True
