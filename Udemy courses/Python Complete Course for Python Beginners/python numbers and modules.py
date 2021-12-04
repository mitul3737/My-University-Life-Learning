"""
0b or 0B : Binary number prefix
0o or 0O : Octal Number prefix
0x or 0X : Hexadecimal number prefix
"""

#checking if 100 is int or float or complex
value=100
print(type(value))
print(isinstance(value,int))
print(isinstance(value,float))
print(isinstance(value,complex))

#checking if 100.24 is int or float or complex
value1=100.24
print(type(value1))
print(isinstance(value1,int))
print(isinstance(value1,float))
print(isinstance(value1,complex))



#checking if 100+5j is int or float or complex
value2=100+5j
print(type(value2))
print(isinstance(value2,int))
print(isinstance(value2,float))
print(isinstance(value2,complex))



print(0b1101)# Ob means binary
print(0xab) #0x means hexadecimal
print(0o23) #0o means octal

#using Decimal module to calculate float point summation , multiplication etc
#1
data=0.1+0.2
print(data)
#solving this issue:
from decimal import Decimal as D
print(D('0.1')+D('0.2'))

#2
data_1=1.20*2.50
print(data_1)
print(D('1.2')*D('2.50'))


#using fraction
from fractions import Fraction as F
print(F(1.5))
print(F(5))
print(F(1,5))


#using math module
import math
print(math.pi)
print(math.cos(10))
print(math.log(10))
print(math.log10(10))
print(math.exp(10))
print(math.factorial(5))
print(math.sinh(10))


#python random module

import random

print('Random number ->',random.randrange(5,15)) #printing any random number between 5 to 15

#choosing something from the list
day_list=['Sat','Sun','Mon','Wed','Thu','Fri']
print(random.choice(day_list))

#shuffling a list
print(day_list)
print(random.shuffle(day_list))
print(day_list)

#any element randomly
print(random.random())