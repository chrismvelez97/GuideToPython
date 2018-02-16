#                       How to use the reverse() method

'''
You might be wondering what the difference is between sort(), sorted(), and
the reverse function.  Well here it is:

[sort() permanently changes the variable to either alphabetical or numerical
order],

[sorted() temporarily changes the variable to either alphabetical or numerical
order],

[reverse() reverses the order regardless of whether or not it is in either
numerical or alphabetical order]
'''

list = ['first', 'middle', 'last']
print (list)
#   results: ['first', 'middle', 'last']

list.reverse()
print (list)
#   results: ['last', 'middle', 'first']
