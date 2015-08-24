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
            if(num2%10 == 1 or num2%10 == 3 or num2%10 == 7 or num2%10 == 9): 
                tempNum=num1*num2 
                if(str(tempNum) == str(tempNum)[::-1]):
                    print(tempNum, " is palindrome!")
                    return tempNum
            num2-=2
        num1-=2 
        
digit=3
start_time = time.time()  
print(findPalindorme(digit)) 
print( (time.time() - start_time), "seconds" )