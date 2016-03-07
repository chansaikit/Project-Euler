'''
Created on Sep 24, 2015

@author: Saikit.Chan
'''


import time 
start_time = time.time()   
tri=0
x=0 
while True:
    x+=1
    tri+=x 
    if len( [n for n in range(1,int(tri**0.5) +1,1) if tri%n==0] )*2 > 500:
        print tri, x
        break
print( (time.time() - start_time), "seconds" )