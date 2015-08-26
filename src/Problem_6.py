'''
Created on Aug 26, 2015

@author: Saikit.Chan
'''
import math
problemNum=100
sumOfSqrt=0
sqrtOfSum=0
for x in range(problemNum):
    sqrtOfSum+=x+1
    sumOfSqrt+=math.pow(x+1, 2)  
print(math.pow(sqrtOfSum, 2) -sumOfSqrt)