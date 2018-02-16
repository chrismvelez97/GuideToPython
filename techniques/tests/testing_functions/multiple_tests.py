                        # Multiple tests
import unittest
from name_functions import format_name

class NamesTestCase(unittest.TestCase):
    '''Multiple test cases'''

    '''Tests first and last name format'''
    def test_first_last_name(self):
        formatted_name = format_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_all_names(self):
        formatted_name = format_name('christian', 'velez', 'michael')
        self.assertEqual(formatted_name, 'Christian Michael Velez')

unittest.main()

'''
Results:

..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK

As shown above, we can now see that both of our tests have passed.

As a result, on line 22 we get two dots to signify that two tests were ran.

Fast forward to line 24, and we can see that it took less than a second to
run our tests.

Finally, on line 26, we get the big OK from our tests stating that our
function is performing as expected.
''' 
