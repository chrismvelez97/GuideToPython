#                               How to use functions

'''
A function is prewritten code that is reuasable.  Let's say you execute some
certain piece of code but you do it multiple times, and it's always the same
code.  If this is true than much like a variable you can store the code in a
function to be executed later.  Functions unlike many data types have to be
declared and you do this using this format:
def foo(bar):
    do something

Just writing the function does not execute the code.  You must actually
call the function after creating this, and although this might seem daunting
the truth is if you've been reading about methods or functions like range() or
slice() those are functions, being called.
'''


def greeting():
    print ("hello world")


#   Notice how we do not say print (greeting) because the code executes the
#   print() function
greeting()
#   Result: hello world
