#                          What is a list?

'''
A list is like variable in the way that it stores other data types but is
different in the way that a variable can only store ONE data type while a list
can store multiple data types.  They are ordered and can be accessed by indices

A list will always start at index 0.

A list can contain any type of data type whether it be a variable, a boolean, a
dictionary, or even another list.  Lists can be modified by accessing
individual indices.
'''
x = 1  # A variable

'''
The list below contains a number, a boolean, a variable, a dictionary, and
another list containing two booleans.
'''

list = [1, True, x, {"key": "value"}, [False, True]]
print (list)
