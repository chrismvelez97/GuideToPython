#                       How to make a list from reading each individual line

'''
When reading from a file, the file object
is only available from within
the block of code that contains the format

with open(filepath) as file_object:
    do something

but if you save the contents in a variable
you can then access that variable outside
the scope of the code block
'''
filepath = '/home/chrismvelez/Desktop/GuideToPython3/techniques/files/file_paths/text_files/readMe.txt'
with open(filepath) as file_object:
    lines = file_object.readlines()
    '''
    As you can see above we introduced another
    function called readlines().

    The readlines() function stores every line
    from the file object as a list which as
    you can see, we have stored in the list
    called lines.
    '''

for line in lines:
    print(line)

#   Above we take that list of lines and run a for
#   loop to see that we have actually retained the
#   information outside the original code block
