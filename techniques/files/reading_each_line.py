#                           How to read a file line by line

'''
Sometimes, because you're analyzing
data for something specific, you'll
want the code to read the file,
line by line.

To do this, you would follow the
normal convention for reading a
file, and instead of printing a
variable contents, you'd run a
for loop scanning each line.

You might notice this produces a
blank line after each line but if
you don't want this you can use
rstrip() as usual.
'''
file_path = "/home/chrismvelez/Desktop/GuideToPython3/techniques/files/file_paths/text_files/readMe.txt"
with open(file_path) as file_object:
    for line in file_object:
        print (line)
