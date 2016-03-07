'''Problem 024
A permutation is an ordered arrangement of objects. For example, 
3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, 
we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''
import time 

def prementation(arr):
    global n
    if len(arr) == 1:
        n=n+1
        if n==stop:
            return arr[0]
    else:
        for i in arr:
            re = str(i)+str(prementation([x for x in arr if not x == i]))
            if n == stop:
                return re
            
start_time = time.time()   
stop=1000000
n=0
arr=[0,1,2,3,4,5,6,7,8,9]
print prementation(arr) 
print( (time.time() - start_time)*1000, 'ms' ) 