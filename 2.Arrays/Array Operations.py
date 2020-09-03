'''we can implement 2.Arrays using Array module which is an inbuilt function in python or we can use List for basic Operations'''
from array import *  # import the function with all the operation

vals = array('i', [])  # i=element type i.e Integer
n = int(input("enter the number of elements:"))  # user input
for i in range(n):
    e = int(input("enter the elements:"))
    vals.append(e)  # insert element

print(vals)

