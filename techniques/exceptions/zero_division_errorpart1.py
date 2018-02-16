#                      How to handle the Zero Division Error

'''
Python can handle most calculations
but it cannot handle calculations that
don't make sense.

One of these mathematical operations
that will not work is dividing any number
by 0.

This will crash our program but here we'll
see how to handle it with exceptions.

First, to identify our error it has to
crash from the error itself so we can
see in our terminal what the error is
named.

I'll paste the traceback below:
>>> print (5/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>>

Now above you can see our error
is called the ZeroDivisionError.

Lets except it in the code below.
'''

try:
    print (5/0)
except ZeroDivisionError:
    print ("You can't divide by zero!")

# Results: You can't divide by zero!


'''
But this block of code just gave us
a print statement!

We want to use exceptions to allow
our code to continue running
despite a fail.

To better show this, see
zero_division_errorpart2.py
'''
