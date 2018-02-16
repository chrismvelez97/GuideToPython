#               How to pass an arbitrary number of arguments

'''
Sometimes, you don't know exactly how many arguments a function is going to
need which is a problem because conditionals require an understanding of what
the parameters are.

Without the conditionals you'll recieve an error for missing number of
arguments so a way around this is to use the * asterisk symbol which basically
tells the computer, "Listen man I have no idea how many arguments this
function will need but just prepare for multiple and the user will fill as
needed"

After the arguments are passed you must loop through them because there might
be multiple arguments.

If you're mixing positional arguments or keyword arguments just always
make sure you're putting the arbitrary arguments last

So to be honest I'm taking most of this information from a book I have, but I
skip over certain things because they're not really neccesary.

To do this, however, I actually need to read and understand everything.  Which
is why it's funny I'm including this because I have no understanding of what
arbitrary means but I understand what the book is trying to say.  I'll look
up the defenition in a dictionary later.
'''


def make_pizza(*toppings):
    print ("\nMaking a pizza with the following toppings")
    for topping in toppings:
        print ("- " + topping)


make_pizza("pepperoni")
'''
Results:

Making a pizza with the following toppings
- pepperoni
'''

make_pizza("pepperoni", "pineapple")
'''
Results:
Making a pizza with the following toppings
- pepperoni
- pineapple
'''
