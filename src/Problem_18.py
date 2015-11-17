'''
Created on Nov 17, 2015

@author: Saikit.Chan
'''
import time, csv

start_time = time.time()  

matrix=[]
with open("../data/problem18_data.csv", "rb") as f:
    reader = csv.reader(f, delimiter =' ')
    for row in reader:
        temp=[]
        for cell in row:
            temp.append(int(cell))
        matrix.append(temp)
        
    for x in range(len(matrix)-1,-1,-1):
        if x == 0:
            print matrix[x]
        else:
            for y in range(len(matrix[x])-1):
                if matrix[x][y] > matrix[x][y+1]:
                    matrix[x-1][y] += matrix[x][y]
                else:
                    matrix[x-1][y] += matrix[x][y+1]  
                    
                    
print "Ran %d Seconds"% (time.time() - start_time)