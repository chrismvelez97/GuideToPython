#                           How to take advantage of file paths

'''
As I mentioned, when I was talking about
reading files, you usually would have your
text file in the same directory.

However, you don't really have to do this.

For example, lets say we were in a folder
called file_paths.
(file_paths)

Lets also say that our python file is in
this directory called file_paths.
(file_paths/relative_paths.py)

Now, lets say we have a sub-directory
inside of file_paths, and inside that
sub-directory we had our text file
(file_paths/text_files/readMe.txt)

What if we wanted to read this file?
Well to do this we'd use those file
paths I've been putting on lines
12,16, and 21.

When we do this, it is called a
relative file path.

With relative file paths, the
computer will always start searching
from whatever directory your python
file is in.
'''

with open('text_files/readMe.txt') as file_object:
    contents = file_object.read()
    print (contents.rstrip())
