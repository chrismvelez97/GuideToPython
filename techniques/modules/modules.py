#                         What is a module

'''
A module is a file that has some functions that you want to use in other files.
This is useful because it hides your source code for the functions and allows,
you to focus on the higher level functionality of your code.

Higher level functionality is what your program is trying to do.
If you imagine functions like tools, you can imagine the code where we define
our functions like the blueprint to build those tools.

We can store the tool and it's blueprint in another file and import it when
we need it so we can just focus on what we're actually  trying to use the tool
for.

It is highly recommended that whenever building out a module you have a comment
at the beginning of the file explaing what the group of classes do, and how to
use them to make it easier for other programmers to use your modules.

For this example we will build the function here and call it in another file
called 'execute_modules.py'
'''


def make_pizza(size, *toppings):
    print ("\nMaking a {0}-inch pizza with the following toppings".format(str(size)))
