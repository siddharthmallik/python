"""
x = lambda a, b : a * b
print(x(9, 7)) 
"""

"""
x = lambda a : a*3 + 3
print(x(8)) 
"""

"""
def square_it_func(a):
    return a * a

x = map(square_it_func, [54, 97, 35])
print(x)
"""

"""
def multiplier_func(a, b):
    return a * b

x = map(multiplier_func, [10, 94, 67], [42, 95, 38])
print(x) 
"""

"""
# numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Function that filters out all numbers which are odd
def filter_odd_numbers(num):

    if num % 2 == 0:
        return True
    else:
        return False

filtered_numbers = filter(filter_odd_numbers, numbers)

print(filtered_numbers)

"""

"""
from itertools import *

# Easy joining of two lists into a list of tuples
for i in 'izip',([1, 2, 3], ['a', 'b', 'c']):
    print ('i')

for i in 'izip',(count(1), ['Bob', 'Emily', 'Joe']):
    print ('i')

def check_for_drop(x):
    print ('Checking: ', x)
    return (x > 5)

for i in 'dropwhile',('should_drop', [2, 4, 6, 8, 10, 12]):
    print ('Result: ', i)


a = sorted([1, 2, 1, 3, 2, 1, 2, 3, 4, 5])
for key, value in groupby(a):
    print((key, value), end=' ')
    


"""


# Using a for loop
numbers = list()

for i in range(1000):
    numbers.append(i+1)
    
total = sum(numbers)
print (total)



"""
# Using a generator
def generate_numbers(n):
     num = 0
     while num < n:
         yield num
         num += 1
         total = sum(generate_numbers(1000))
         print (total)
"""

"""
total = sum(range(1000 + 1))
#total = sum(xrange(1000 + 1))
print (total)
"""