#                       How to use the pop() method

'''
Pop removes an item from a list.  When the pop() function isn't given an
argument it just removes the last one.  When given an argument like pop(foo)
it will will remove at that index.  So why should you use pop instead of del?
Well pop allows you to save the removed value in a variable as you're about to
see.
'''

motorcycle = ['honda', 'yamaha', 'suzuki']
print (motorcycle)
#   results: ['honda', 'yamaha', 'suzuki']

#   Ex.1
motorcycle.pop()
print (motorcycle)
#   results: ['honda', 'yamaha']

#   Ex.2
motorcycle.pop(0)
print (motorcycle)
#   results: ['yamaha']

#   Ex.3
saved = motorcycle.pop()
print (motorcycle)
#   results: []

print (saved)
#   results: 'yamaha'
