#                           How to append to files

'''
Previously, we mentioned how just
writing to a file is dangerous, for
the reason that if that file has
information, it will all get deleted
and rewritten into whatever you'd
like or passed into your write()
method

Luckily enough for us, there is also
an append mode.

Just like with the write technique,
you must add an extra argument to
the open() function, but this
time the second argument will be
passing will be the 'a' mode.

The append mode allows you to add
to an existing document without
overwriting the file with your
write argument.

If the file path specified is non
existent, then a new file will
be created with that name.
(See Ex.2)
'''
#   Ex.1
file_path = '/home/chrismvelez/Desktop/GuideToPython3/techniques/files/appendingFiles/text_files/readMe.txt'
with open(file_path, 'a') as f_object:
    '''
    Below, you can see that we still use the write() method.
    I believe this to mean that the 'a' method has a different,
    but similiar way of adding txt to a file.
    '''
    f_object.write("\nI also love finding meaning in large datasets.\n")
    f_object.write("I also love creating apps that can run in a browser.\n")


#   Ex.2
file_path = '/home/chrismvelez/Desktop/GuideToPython3/techniques/files/appendingFiles/text_files/newFile.txt'
with open(file_path, 'a') as f_object:
    '''
    You can't tell this now, but Previously the file named
    newFile.txt did not exist. We created it with this
    bit of code:
    '''
    f_object.write("This is a brand new file.")
