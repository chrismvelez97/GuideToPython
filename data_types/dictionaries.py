#                           How to use dictionaries

'''
Dictionaries are special forms of containers that do NOT have indices.  They
can start off empty and have values added later

Instead, they have key and value pairs.  To access a value you use the key.

The keys must be strings, and the values can hold anything from variables to
lists, to even other dictionaries.

A dictionary can be looped through but it will not be in order since they have
no indices.

Lastly, every single key is unique meaning you cannot use it again within the
same dictionary.
'''
dictionary = {
    "words": {
        "penultimate": "The second to last item in a group.",
        "ultimate": "The last item in a group"
    },
    "numbers": {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5
    },
    "extra": "value"
}

print (dictionary["words"])  # How you access dictionary values
'''
Results:
{'penultimate': 'The second to last item in a group.',
'ultimate': 'The last item in a group'}
'''

print (dictionary["words"]["penultimate"])
#   results: The second to last item in a group.

print (dictionary["numbers"])
#   results: {'one': 1, 'three': 3, 'two': 2, 'five': 5, 'four': 4}

# How you add values to dictionaries
dictionary["booleans"] = [True]
print (dictionary["booleans"])
#   results: [True]

# How you modify values in dictionaries
dictionary["booleans"] = [True, False]
print (dictionary["booleans"])
#   results: [True, False]

# How you delete keys in dictionaries
del dictionary["extra"]
