'''
Created on Aug 24, 2015

@author: Saikit.Chan
'''

import time
import math


def findPalindorme(digit):
    num1=int(math.pow(10, digit) -1)
    minNum= num1 - math.pow(10, digit-1) 
    while(num1>minNum):
        num2=num1
        while(num2>minNum):
            d=num2%10
            if(d == 1 or d == 3 or d == 7 or d == 9): 
                tempNum=num1*num2 
                if(str(tempNum) == str(tempNum)[::-1]):
                    print(tempNum, " is palindrome!")
                    return tempNum, num1, num2
            num2-=2
        num1-=2 
        
digit=3
start_time = time.time()  
print(findPalindorme(digit)) 
print( (time.time() - start_time), "seconds" )