#                           How to read files using python3

#   Note that this file is linked to lorepIpsum.txt

with open('lorem_ipsum.txt') as file_object:
    '''
    The open function above, opens the file.
    Anytime you access a file you must always,
    use the open function.  It takes in one
    parameter and that is the file name.
    Finally, the open() function returns the
    text in your file as an object.  It then
    stores that object inside of the file_object.

    Also, above is the word 'with'.  This keyword
    closes access to the file once our program
    no longer needs it.  You could technically
    close using the close() function but as it
    was taught to me, that method is extremely
    dangerous as it is prone to data loss, and
    corruption.

    The file you're trying to execute must,
    for now at least, be in the same directory
    as your python file.
    '''
    contents = file_object.read()
    '''
    Here in the code above, we execute our read()
    function that returns the entire file contents
    as a string with an extra blank line at the
    end.

    To get rid of this line you can use the rstrip()
    function.

    After executing the read() function, we store
    that string into the variable contents.
    From there we print it out to the console.

    It should be noted that all read text files get
    returned as strings.
    '''
    print (contents)

        '''
        After going online to do some
        research I've found that an error
        called UnicodeDecodeError might pop
        up when trying to read files like this.

        For me, at the time of making this guide,
        it read fine when executing from the terminal
        but just to be safe the new way to do this
        is as follows.
        '''
filename = 'lorem_ipsum.txt'

try:  # You don't really need the try but you can have it
    with open(filename, encoding='utf-8') as f_obj:
        # As you'll notice we now have an extra argument
        # being passed name 'utf-8' which is the encoding
        # of most text files.
        # The parameter is also called encoding.
        contents = f_obj.read()
