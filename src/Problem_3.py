'''
Created on Aug 21, 2015

@author: Saikit.Chan
''' 
import time
import math

number=600851475142

def findPrime(num): 
    prime=1 
    i=2
    while(i < math.sqrt(num)):
        j = 2
        while(j <= (i/j)):
            if not(i%j): break
            j = j + 1
        if (j > i/j and num%i==0): 
            prime=i
            temp=findPrime(num/i)   #you can comment out these code to see different
            if(temp>prime):         #you can comment out these code to see different
                prime=temp          #you can comment out these code to see different
                break               #you can comment out these code to see different
        if(i>2):
            i+=2
        else:
            i+=1
    
    if(prime==1):
        prime=num
    return prime

start_time = time.time()  

print("Biggest Prime: ", findPrime(number))

print( (time.time() - start_time), "seconds" )