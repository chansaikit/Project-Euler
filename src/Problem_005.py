'''
Created on Aug 24, 2015

@author: Saikit.Chan
'''
import math
def getPrimeList(num): 
    primeList=[]
    i=2
    while(i < num):
        j = 2
        while(j <= (i/j)):
            if not(i%j): break
            j = j + 1
        if (j > i/j ): 
            primeList.append(i)
        if(i>2):
            i+=2
        else:
            i+=1
    return primeList 

def test(num):
    for i in range(1,20):
        if num%i != 0 and (num/i)%2 != 0:
            return False 
    return True

array=[]
problemNum=20
total=1
primeList = getPrimeList(problemNum) # get prime list
print(primeList)
 
for i in range(problemNum+1): 
    array.append(0)
    if i > 1:
        num=i
        for prime in primeList:
            counter=0
            while(num%prime == 0):
                num/=prime
                counter+=1 
            if(counter>0 and array[prime]<counter):
                array[prime]=counter

print(array)
for x in range(problemNum+1):
    total = total * math.pow(x, array[x])  
print("Check smallest positive number " + str(total) + " :" + str(test(total)))
# answer=232792560