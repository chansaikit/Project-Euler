def sumOfDiv(num):
    if num < 220: # first Amicable numbers is 220
        return -1
    a = range(2,int(num**0.5)+1)   
    out=[1] 
    for x in a:
        if x == 0:
            continue
        if (num  % x) > 0:  
            a[x-2::x]=[0]*int((len(a)+1)/x) # flag out the unmatch number and its multiples 
        else:
            out.append(x) #adding the divisors to list
            out.append((num/x)) 
    return sum(out) 
 
total =0
x=2
while x < 10000: 
    temp = sumOfDiv(x) 
    if(temp > x and x == sumOfDiv(temp)):
        total = total + x + temp
        print x, temp
        x=temp
    x=x+2
        
print "sum:",total