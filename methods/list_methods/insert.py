#                       How to use the insert method

'''
The insert() method is actually very similiar to the append() method.
The only difference is that insert takes in two arguments.  It takes
in the position that you would like to insert, otherwise known as the
index, and it also taks in the value you'd like to insert.
The setup is as follows: variable.insert(index, value)
'''
motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)
# results: ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print (motorcycles)
# results: ['ducati', 'honda', 'yamaha', 'suzuki']
