#                       How to use the remove() method

'''
The remove() method removes a value based on a value given. It searches through
the list and removes the very first value that matches the one given in the
argument.
'''

motorcycle = ['honda', 'yamaha', 'suzuki', 'ducati']
print (motorcycle)
#   results: ['honda', 'yamaha', 'suzaki', 'ducati']

motorcycle.remove('ducati')
print (motorcycle)
#   results: ['honda', 'yamaha', 'suzaki']
