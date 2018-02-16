#                       How to use the min() function

'''
The min function grabs the smallest number in any set of numbers.

Note that for min, max, and sum, you can only do them on lists full of numbers.
also it is not a method attached to the number datatype which is why it is in
the techniques folder instead of the num_methods folder.
'''
numbers = list(range(11))  # Here the list() function allows us to create a list from range()
print (numbers)
#   results: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print (min(numbers))
#   results:0
