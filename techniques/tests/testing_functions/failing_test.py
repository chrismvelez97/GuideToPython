                    # Our failing test case

# Importing the module we want to use to test
import unittest

# importing the function we want to test
from name_functions import format_name

class NamesTestCase(unittest.TestCase):
    '''A failing test case for the names function'''

    '''Tests the first, middle, and last name'''
    def test_first_middle_last_name(self):
        formatted_name = format_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()

'''
Results:
E
======================================================================
ERROR: test_first_middle_last_name (__main__.NamesTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "failing_test.py", line 14, in test_first_middle_last_name
    formatted_name = format_name('janis', 'joplin')
TypeError: format_name() missing 1 required positional argument: 'last'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)

As you can see above this test actually failed.  As a result we get the
capital E on line 21 which tells us that one of our tests resulted in an error.

On line 23, we can see exactly which of our tests failed, which is useful
for when we start creating multiple tests.

On lines 25-28 we get back the error message, so we can figure out where the
error began and what kind of error it was.

Lastly, line 31 told us how many of our tests were ran and how long it took, and
line 33 told us that our test FAILED and how many errors there were.

All of this information is extremely valuable as you can see in providing
pinpoint accuracy to find our error and fix it which is why testing is so
popular and useful.

It should be noted that when you get a FAILED message because you have errors,
it means you should fix your code that you're testing and NOT the test itself.

For example we'd want to go back into wherever our name function is and resolve
it there rather than here, because the errors live within the function.
'''
