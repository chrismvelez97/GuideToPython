#                           How to write into an empty file

'''
Eventually, after analyzing
so much data you'll want to save it
to a seperate file.

To do this, you have to include an
extra argument in the open() function
that tells the function you want to
write to the file.

Understand that if you use the write
mode, python will delete whatever
is in the file you're trying to write
to and put in your write argument.

Also note that with multiple lines,
python will not create new lines from
each different write. Instead the text
will be inline, but you can easily
change this with '\n' for newline or
'\t' for tab. See:
(/GuideToPython3/techniques/adding_whitespaces.py)

'''
write_file = '/home/chrismvelez/Desktop/GuideToPython3/techniques/files/writingFiles/text_files/emptyFile.txt'
with open(write_file, 'w') as f_object:
    '''
    You can see above the form is similiar
    two reading a file, but now we have
    a second parameter where we pass the
    argument 'w' which means to write to.

    Down below, you can see that whatever
    we named out file object has a method
    we can use called write() which takes
    in an argument, which is whatever we'd
    like to write to the file.
    '''
    f_object.write("Hello World")
