print reduce(lambda x,y:x+y, [int(x) for x in str(reduce(lambda x, y: x*y,  range(1,100)))])
    