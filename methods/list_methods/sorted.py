#                       How to use the sorted() method

'''
Sorted works almost exactly like the sort() method with the exception
that the state of change is not permanent.  After the method is executed the
order will reverse back to whatever it was.  This is good for presenting
information in a certain order.  You can still use sorted() to reverse lists
but in order to do this you must tack on a second argument like so:
sorted(foo, reverse=True)
Lastly, a good thing to note is that, instead
of this function being a method attributed to the list like so: foo.sorted()
we executed it like this sorted(foo).
'''
cars = ['bmw', 'audi', 'chevy']
print (cars)
#   results: ['bmw', 'audi', 'chevy']

#   Below you'll notice we executed the function inside of the print function
#   So as to not lose the sort
print(sorted(cars))
#   results: ['audi', 'bmw', 'chevy']

print(sorted(cars, reverse=True))
#   results: ['chevy', 'bmw', 'audi']
