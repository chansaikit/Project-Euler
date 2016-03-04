import time 

#using brute force to find divisor 
def sumOfDiv(num):
    a = range(2,int(num**0.5)+1)   
    out=[1] 
    for x in a:
        if x == 0:
            continue
        if (num  % x) > 0:  
            a[x-2::x]=[0]*int((len(a)+1)/x) # flag out the unmatch number and its multiples 
        else:
            out.append(x) #adding the divisors to list
            if not num/x == x:
                out.append((num/x)) 
    return sum(out) 

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

#########################################
#using prime to find the sum of divisors
# n = prime**a
#SumOfDivisors(n) = (prime**(a+1)-1) / (prime - 1)
#reference:
#http://www.mathblog.dk/project-euler-21-sum-of-amicable-pairs/
#########################################
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
    return sum - n
  
    
start_time = time.time()   
total =0
limit=100000+1
x=2
primeList=getPrimeList(limit)

while x < limit: 
    temp = sumOfDivisors(x, primeList) 
    if(temp > x and x == sumOfDivisors(temp, primeList)):
        total = total + x + temp
        print x, temp
        x=temp
    x=x+2

print "sum:",total
print( (time.time() - start_time)*1000, 'ms' ) 