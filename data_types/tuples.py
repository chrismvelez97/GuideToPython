#                          What is a tuple?

'''
A tuple works almsot exactly like a list except with two minor exceptions.

A list has brackets like so:
x = [1, 2, 3]

but a tuple has parenthesis like so:
x = (1, 2, 3)

With a list you can access the list like so: foo[0] and then change values like
that.  A tuple will not allow you to do this because they are immutable,
meaning you cannot modify them through accessing their indices.

You can however, redefine the tuple but that is the only way you can change a
tuple.

x = (1, 2, 3)
x[0] = True  # Will not work

The above example will give this error:
Traceback (most recent call last):
  File "/home/chrismvelez/Desktop/python3_practice/data_types/tuples.py",
  line 20, in <module>
    x[0] = True  # Will not work
TypeError: 'tuple' object does not support item assignment
'''
x = list(range(1, 6))
print (x)
#   results: [1, 2, 3, 4, 5]

x = list(range(6, 11))
print (x)
#   results: [6, 7, 8, 9, 10]
