'''
Created on Aug 27, 2015

@author: Saikit.Chan
'''


import time 
start_time = time.time()    

def sumPrime(limit):   
    primeList=[True] * limit 
    total=2
    for i in range(3, int(limit**0.5)+1,2):
        if primeList[i]: 
            primeList[i*i::2*i]  = [False] * int((limit-i*i-1)/(2*i)+1) 
    for i in range(3,limit,2):
        if primeList[i]:
            total+=i
    return total
 
print(sumPrime(2000000)) 
print( (time.time() - start_time), "seconds" )