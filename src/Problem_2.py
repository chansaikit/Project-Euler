'''
Created on Aug 18, 2015

@author: Saikit.Chan
''' 
import time


total = 2 #base case
dict = {1:1, 2:2}
maxNum=4000000
a=1
b=1 

#method 1
def fibonacci(deep):
    global total
    global maxNum
    if deep in dict:
        return dict[deep]
    else:
        dict[deep] = fibonacci(deep-1) + fibonacci(deep-2)
    if dict[deep] > maxNum:
        return dict[deep]
    if dict[deep]%2 == 0:
        total += dict[deep]
    return(dict[deep])

start_time = time.time()   
print(fibonacci(50))
print ("total = " ,total) 

#method 2
total=0
while(total<maxNum):
    c=b
    b=a+b
    a=c 
    if a%2==0:
        total += a  
print ("total = " ,total) 

print( (time.time() - start_time), "seconds" )