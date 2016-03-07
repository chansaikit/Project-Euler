'''
Created on Oct 22, 2015

@author: Saikit.Chan
'''


import time    

def findTerm(num,numTable):
    counter=1
    while(num!=1): 
        num=num/2 if num&1 else (3 *num) +1
        counter+=1
    return counter


start_time = time.time()   
ans=0
num=1000000
numTable={}
longest=0
for x in range(num,(num/2 -1),-2): 
    term=findTerm(x,numTable)
    if term>longest:
        longest=term
        ans=x
print ans, longest
    
print "Ran %d Seconds"% (time.time() - start_time)