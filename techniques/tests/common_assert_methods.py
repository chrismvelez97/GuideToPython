# Wow my programming actually came in handy.  It took me less time to code this
# than to type this.

# execute file to get readable data on common assert assert_methods
assertEqual = "Used to verify that the outcome of your code is equivalent to what you expected"
assertNotEqual = "Used to verify that the outcome of your code is NOT equal to what you expected"
assertTrue = "Makes sure that something is true"
assertFalse = "Makes sure that something is False"
assertIn = "Asserts that an item is in a list"
assertNotIn = "Asserts that an item is NOT in a list"
assert_methods = {
    "assertEqual": [assertEqual, ["function outcome", "outcome expected"]],
    "assertNotEqual": [assertNotEqual, ["function outcome", "outcome expected"]],
    "assertTrue": [assertTrue, ["function outcome"]],
    "assertFalse": [assertFalse, ["function outcome"]],
    "assertIn": [assertIn, ["item", "list we're checking"]],
    "assertNotIn": [assertNotIn, ["item", "list we're checking"]],
}

for key, value in assert_methods.items():
    print("Method: {0}\nDefinition: {1}\nArguments: {2}\n".format(key, value[0], value[1]))
