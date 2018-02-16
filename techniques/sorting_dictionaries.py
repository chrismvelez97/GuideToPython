#                        How to use the sort dictionaries

'''
Earlier, I mentioned that dictionaries do not return keys in any particular
order when looping through them.

While this is true, you can use the sorted() function to sort the results
alphabetically, since all keys are strings.
'''
favorite_languages = {
    "jen": "Python",
    "sarah": "C",
    "edward": "ruby",
    "phil": "python"
}

for name in sorted(favorite_languages.keys()):
    print (name.title())

'''
Results:
    Edward
    Jen
    Phil
    Sarah
'''
