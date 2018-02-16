#                           How to save user data
'''
Using the json.dump() and json.load()
techniques we just learned about, we
can actually save user data to be
used at a later time.
'''
import json

username = input("Hello! What is your name?\n\n")

path = "/home/chrismvelez/Desktop/GuideToPython3/techniques/files/storingData/jsonFiles/user_data.json"
with open(path, 'w') as fobject:
    json.dump(username, fobject)
    print("\nWe'll remember you when you come back now!")

with open(path) as fobject:
    jsonData = json.load(fobject)

    reply = input("You said your name was {0} right?\n\n".format(jsonData))

    if reply == 'y':
        print ("okay good")
    elif reply == 'n':
        print ("Sorry about that!")
