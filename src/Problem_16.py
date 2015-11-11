'''
Created on Nov 11, 2015

@author: Saikit.Chan
'''

import time 

start_time = time.time()  

print sum( [int(x) for x in str(2**1000)])

print "Ran %d Seconds"% (time.time() - start_time)