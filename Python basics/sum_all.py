list = [4,3,2,5,3,5,4,2,4]

def getSum():
    total = 0
    for item in list:
        total = total + item
    return total

print(getSum())