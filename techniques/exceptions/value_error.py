#                    How to handle the value error

'''
The value error is when your
program is expecting a certain
value type back such as a number
or a string and you get the other.

For example, we'll be using a
calculator that can add, but
get a value error if we type letters
in place of numbers.

The following is the error
we'd see for strings:

First Number: d
Second Number: d
Traceback (most recent call last):
  File "value_error.py", line 23, in <module>
    answer = int(f_num) + int(s_num)
ValueError: invalid literal for int() with base 10: 'd'

'''
print ("Give me two letters to add.\nPress 'q' to quit")

while True:
    f_num = input("\nFirst Number: ")
    if f_num == 'q':
        break
    s_num = input("Second Number: ")
    if s_num == 'q':
        break
    try:
        answer = int(f_num) + int(s_num)
    except ValueError:
        print ("\nYou can't enter letters to add!\nPress 'q' to quit or try again.")
    else:
        print ("Answer: " + str(answer))
