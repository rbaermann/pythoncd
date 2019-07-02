def countdown(num):
    newList = []
    for i in range (num, -1, -1):
        newList.append(i)
    return newList
print(countdown(5))

def printAndReturn(list):
    print(list[0])
    return(list[1])
print(printAndReturn([2,7]))

def firstPlusLen(list):
    return (list[0] + len(list))
print(firstPlusLen([1,2,3,4,5]))

def valGreaterThanSec(list):
    newList = []
    count = 0
    if(len(list) < 2):
        return False
    else:
        for i in range (0, len(list)):
            if(list[i] > list[1]):
                newList.append(list[i])
                count += 1
    print(count)
    return newList
print(valGreaterThanSec([5,2,3,2,1,4]))
print(valGreaterThanSec([3]))

def thisLenThatVal(size, val):
    newList = []
    for i in range (size):
        newList.append(val)
    return newList
print(thisLenThatVal(4,7))
print(thisLenThatVal(6,2))