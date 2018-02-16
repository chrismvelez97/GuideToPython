#                       How to use the del method

'''
The del method is executed a bit different than what we've seen so far.
Instead of the regular 'function()' setup you can just use del as it is.
You must know, however, exactly what index you'd like to delete.
'''
motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)
#   results: ['honda', 'yamaha', 'suzuki']

del motorcycles[0]
print (motorcycles)
#   results: ['yamaha', 'suzuki']
