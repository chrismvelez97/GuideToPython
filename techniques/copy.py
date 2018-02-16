#                        How to use the copy technique in python

'''
So this might be a little confusing but I'll try to make it understandable.
Copy creates an exact copy of whatever list you're copying. This is the format:

x = [1, 2, 3]
y = x[:]

So the part that might be confusing is why must we use this method, when we can
instead do something like this:

x = [1, 2, 3]
y = x

Well the reason for that is that in the second case, we are telling python that
y is whatever x is.  We are pointing to the value of x rather than copying the
info.  See the Ex.2 for a more thorough explanation on why the above example
doesn't work.
'''

#   Ex. 1
x = [1, 2, 3]
y = x[:]
y.append(4)
print (x)
#   results: [1, 2, 3]

print (y)
#   results: [1, 2, 3, 4]


#   Ex. 2
# x = [1, 2, 3]
y = x  # Here we point to the value of x
y.append(4)
print (x)
#   results: [1, 2, 3, 4]
'''
If you see above at Ex.2, when we appended 4 to y it also added the number 4 to
x, when our actual intended output was for us to have x remain as it was and
y have a copy of x, with y as well as in Ex.1
'''
