                        # Our passing test case
# Importing python native module unittest
import unittest

# Importing our function from the name_functions file
from name_functions import format_name

'''
Below this class will contain our tests for our
format_name function.

We can technically name this class whatever we
want, but it is best to name it related to your
function, and with the word test in it.
'''
class NamesTestCase(unittest.TestCase): # Our class inherits from unittest.TestCase
    '''A passing test case for the names function'''

    '''Tests the first name and last name format'''
    def test_first_last_name(self):
        '''Do names like Janis Joplin work?'''
        formatted_name = format_name("janis", "joplin")

        '''
        Here Below on line 35, we used the assertEqual()
        method.  This method makes sure that our outcome
        of our code is equal to the outcome of what we
        expected.

        The two arguments are our code that we're
        testing, and the outcome we expect hence the
        result of our function (formatted_name) followed
        by the outcome we expect('Janis Joplin')
        '''
        self.assertEqual(formatted_name, "Janis Joplin")

unittest.main()

'''
This is extra but I'm including it for the reason that
the results of unittest.main(), which runs our tests,
provide some useful information.

.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

The first dot on line 44, tells us that one of our tests passed.
The next piece on line 46, tells us that how many tests we ran,
and how long it took to run the code.

Lastly, on line 48, we see that string 'OK' tells us that every
single one of our tests passed.

From now on we know that when our function takes in names it
will always be able to handle first name, last name formats.

This is helpful because in the future if we ever want to
modify our function, we can just run our test to make sure that
our code still works for the first name, and last name, format.
'''
