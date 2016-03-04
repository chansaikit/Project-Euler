'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

'''

import time 

#reuse the code from problem 21
#using brute force to find divisor 
def sumOfDiv(num):
    if num < 12: # first Abundant numbers is 12
        return False
    a = range(2,int(num**0.5)+1)   
    out=1 
    for x in a:
        if x == 0:
            continue
        if (num  % x) > 0:  
            a[x-2::x]=[0]*int((len(a)+1)/x) # flag out the unmatch number and its multiples 
        else:
            out=out+x #adding the divisors to list
            if not num/x == x:
                out=out+(num/x)  
    return True if out > num else False 

#reuse the code from problem 10
def getPrimeList(limit):   
    primeList=[True] * limit  
    list=[2]
    if limit < 2:
        return []
    for i in range(3, int(limit**0.5)+1,2):
        if primeList[i]: 
            primeList[i*i::2*i]  = [False] * int((limit-i*i-1)/(2*i)+1) 
    for i in range(3,limit,2):
        if primeList[i]:
            list.append(i)
    return list

#reuse the code from problem 21
def sumOfDivisors(num, primeList):
    n=num
    sum=1
    if num > 2:
        for prime in primeList:
            if prime**2 > num:
                break
            else:
                if num % prime == 0:
                    p = prime * prime
                    num = num / prime
                    while num % prime == 0:
                        num = num / prime
                        p = p*prime
                    sum = sum * (p-1) / (prime-1)
    if num > 1:
        sum=sum*(num+1)
    return True if (sum - n) > n else False


start_time = time.time()   

size=20161 +1
primeList= getPrimeList(size) 
  
abundant=[]
for x in range(12, size):
    if(sumOfDivisors(x, primeList)):
    #if(sumOfDiv(x)):  #brute force
        abundant.append(x) 
abundant=(list(abundant)) 
print 'Numer of Abundant Numbers', len(abundant)  
a=range(0, size)
for y in range(len(abundant)):
    for x in range(y,len(abundant)):
        if (abundant[x] + abundant[y]) >= size:
            break
        else: 
            a[abundant[x] + abundant[y]] = 0
      
print 'Sum of all the positive integers which cannot be written as the sum of two abundant numbers:', sum(a)

print( (time.time() - start_time)*1000, 'ms' ) 