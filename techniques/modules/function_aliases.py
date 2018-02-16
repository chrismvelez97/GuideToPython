#                           What are function aliases?

'''
Sometimes, you're going to import a function that has a name that is either too long, or conflicts
with a function name in your current file.

To avoid this you can give your function an alias to refer to easier when using dot notation.

For the following example we will import make_pizza() from modules.py and give it the alias
mp so we don't have to continually type out make_pizza.

This also allows us to get away with not using the dot notation as you'll notice
'''
from modules import make_pizza as mp

mp(5, "pepperoni")
#   results:    Making a 5-inch pizza with the following toppings
