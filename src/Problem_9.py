'''
Created on Aug 27, 2015

@author: Saikit.Chan
'''

import time 
start_time = time.time()   

problemNum=1000
for i in range(2,problemNum):
    for j in range(i,problemNum-i): 
            k=problemNum-i-j
            if i*i+j*j==k*k:
                print(i,j,k, "Answer: %d" %(i*j*k))
                print( (time.time() - start_time), "seconds" )
                exit()
