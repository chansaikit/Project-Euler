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
            for x in range(i*2,limit,i):
                primeList[x]=False 
    for i in range(3,limit,2):
        if primeList[i]:
            total+=i
    return total
 
print(sumPrime(1000000)) 
print( (time.time() - start_time), "seconds" )