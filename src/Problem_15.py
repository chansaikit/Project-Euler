'''
Created on Oct 27, 2015

@author: Saikit.Chan
'''

import time


def start(x, y, size, Matrix):
    if x == size or y == size:
        return 1
    if Matrix[x][y] == 0:
        Matrix[x][y] = start(x+1, y, size,Matrix) + start(x,y+1,size,Matrix)
    return Matrix[x][y]

start_time = time.time() 
size=20
Matrix = [[0 for x in range(size)] for x in range(size)] 
start(0,0,size,Matrix) 
print Matrix[0][0]

print "Ran %d Seconds"% (time.time() - start_time)