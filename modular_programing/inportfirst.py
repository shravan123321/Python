# featching the file modularfirst.py file
'''
# first method access the another file
import modulfirst

print(modulfirst.sum(10,20))
print(modulfirst.subtraction(20,10))

'''

'''
# second methods access the another file
import modulfirst as m

print(m.sum(10,10))
print(m.multiplaction(10,10))
print(m.subtraction(10,10))

'''

'''
# third methods access the enother file

from modulfirst import sum, subtraction

print(sum(10,10))
print(subtraction(10,10))
# Ager hum multiplaction function ko access karna chahta hu to aush time humko code me Error indicated karega qki humne multion function ko indicate nahi kiye hai
# print(multiplaction(10,10))
'''

# fourth methods to access the another file 
# Ager  hum ke total function ko access karna hai but ausha name nahi dena hai to aush time  hum sirf * laga dete hai

from modulfirst import *

print(f"sum of two number: {sum(10,10)}")
print(f"Two number Subtraction: {subtraction(20,10)}")
print(f"Multiplaction of two number: {multiplaction(10,10)}")
print(f"cube number: {cubenum(10)}")
'''


# five methods to access the another file 

# importing sys module
import sys

# importing sys.path
print(sys.path)

'''