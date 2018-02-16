#                           How to loop Dictionaries

'''
You can loop through dictionaries but it should be noted that they will not
come out in any specific order because are not ordered by indices
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
    "booleans": [True, False]
}

#   How to print just the keys
for key in dictionary:
    print (key)
'''
Results:

numbers
booleans
words
'''

#   How to print the key, value pairs
user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi"
}

for key, value in user_0.items():  # You need the item() method to print both
    print ("\nKey: " + key)
    print ("\nValue: " + value)

'''
Results:

    Key: first

    Value: enrico

    Key: last

    Value: fermi

    Key: username

    Value: efermi
'''
