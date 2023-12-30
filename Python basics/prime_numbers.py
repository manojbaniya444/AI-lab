for i in range (1,100):
    isNotPrime = False
    if i > 1:
        for j in range(2,i):
            if (i % j == 0):
                isNotPrime = True
        
    if (not isNotPrime):
        print(i)
