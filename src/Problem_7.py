'''
Created on Aug 26, 2015

@author: Saikit.Chan
'''
import math
import time
primeList=[2]
def getPrime(pos):  
    i=2
    global primeList
    counter=1
    while(i > 1):
        j = 2
        half=math.sqrt(i)
        for j in primeList: 
            if not(i%j) or j > half: break 
        if (j > i/j ): 
            primeList.append(i)
            if pos==counter:
                return i
            counter+=1
        if(i>2):
            i+=2
        else:
            i+=1

print(getPrime(10001)) 
print( (time.time() - start_time), "seconds" )
