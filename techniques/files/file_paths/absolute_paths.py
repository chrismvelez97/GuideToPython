#                                 How to use absolute paths

'''
Absolute paths are the entire pathway
from the home directory all the way down
to the exact location of your file.

Usually, absolute paths are very long so
sometimes it's helpful to store them
in variables.
'''
file_path = "/home/chrismvelez/Desktop/GuideToPython3/techniques/files/file_paths/text_files/readMe.txt"
with open(file_path) as file_object:
    contents = file_object.read()
    print (contents.rstrip())
