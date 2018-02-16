#                    How to loop through lists inside a dictionary

'''
I created this file because I think earlier I came across an error that
mentioned something about how looping through dictionaries and lists is
different.  So if you have a list in a dictionary this is how you would loop
through it.

If you have multiple type of data types in your dictionary I'd suggest using
conditionals to check what type of data type the dictionary key is containing,
and based on what it is, you can run a different kind of looping strategy
'''
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"]
}

for topping in pizza["toppings"]:
    print (topping)
'''
Results:
    mushrooms
    extra cheese
'''
