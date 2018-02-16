#                       How to use the sort() method

'''
Sort allows us to sort our list alphabetically or numerically.
It should be noted, however that it permanently sorts the list so
you lose the original order.  You can
also do a reverse sort by adding an arguemnt.
'''

alphabet = ['b', 'a', 'c', 'e', 'd']
print (alphabet)
#   results: ['b', 'a', 'c', 'e', 'd']

alphabet.sort()
print (alphabet)
#   results: ['a', 'b', 'c', 'd', 'e']

alphabet.sort(reverse=True)
print (alphabet)
#   results: ['e', 'd', 'c', 'b', 'a']
