#                    How to use json.dump() & json.load()
import json

'''
Sometimes you'll want to store user, information
to be used for later.

To do this, we save the have to import the json
module, to access json.dump() and json.load(),
and we'll also have to be in 'w' mode otherwise
known as 'write' mode.

We use json.dump() to dump the data into the json
file.
json.dump() takes two arguments.

The first, is the data you'd like to store.
The second is the file path to the json file
to store it to.

We use json.load() to access the json files data.
json.load() only takes one argument and that is
the file object.
'''
numbers = list(range(1,11))
file_path = "/home/chrismvelez/Desktop/GuideToPython3/techniques/files/storingData/jsonFiles/num_to_100.json"

with open(file_path, 'w') as f_object:
    json.dump(numbers, f_object)

# Now that we've dumped our data, lets display it back
with open(file_path) as f_object:
    jsonFile = json.load(f_object)

print (jsonFile)
