'''
Created on Oct 20, 2015

@author: Saikit.Chan
'''

import csv,time 
start_time = time.time()   
total=0 
with open('../data/problem13_data.csv','rb') as f:
    reader = csv.reader(f)  
    for num in reader:   
        total+=int(num[0])  
print str(total)[0:10]

print "Ran %d Seconds"% (time.time() - start_time)