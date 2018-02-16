#                        How to use the slice technique in python

'''
Slice is a technique that can be used to cut a list from a specific starting
index to a specific ending index.  Everything NOT SPECIFIED in the arguments
will be temporarily removed.

Much like with range() the starting argument is where you begin but the ending
ending is one ahead of where your slice will end.

Also much like range()
ommitting the first argument like so foo[:10] will just start the cut at the 0
index.

Ommitting the second argument like so foo[2:] will cut from that argument until
the end of the list

Lastly, using a negative number as the first argument like so foo[-1] will cut
from the last index.  Increasing that number will do the same so cutting from
foo[-2] will cut from the penultimate index over to the last index.

It should be noted that in the title for this file, I said technique and noted
method or function.  Although it is a function, and it is somewhat of a method
because you do use it almost exclusively for lists, it is different in the fact
that you do not call slice in the two ways we have seen.

Ex.
You would not say slice(foo)

Ex.
You would also be incorrect to say foo.slice()

Ex.
foo[start:end] is the correct way to use slice.
'''

list = list(range(11))
print (list)
#   results: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print (list[2:10])

'''
Notice we started at the third spot because indexes start at 0
and we ended one index before the tenth index, essentially cutting
the beginning two, followed by the ending off from the previous list.

results: [2, 3, 4, 5, 6, 7, 8, 9]
'''
print (list[:10])
#   Here you can see ommitting the first arg started the cut at 0 index
#   results: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print (list)  # Here you can see the list returns to its original form

print (list[-1:])
#   results: [10] Here you can see that we get returned the last index
