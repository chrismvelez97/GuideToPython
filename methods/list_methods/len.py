#                       How to use the len() method

'''
The len() function is another one of those functions that isn't a method
attached to the list constructor.  This basically means you use the variable
as an argument rather than using the dot notation.  len() also returns the
amount of indexes in the list.
Basically:
len(foo) is correct
foo.len() is not
'''

list = [1, 2, 3, 4, 5, 6, 7]
print(len(list))
#   results: 7
