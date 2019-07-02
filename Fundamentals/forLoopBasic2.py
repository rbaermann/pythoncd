def biggieSize(list):
    for i in range (len(list)):
        if(list[i] > 0):
            list[i] = 'big'
    return list
biggieSize([-1,3,4,-5])

def countPos(list):
    count = 0
    for i in range (len(list)):
        if(list[i] > 0):
            count += 1
    list.pop()
    list.append(count)
    return list
countPos([-1,1,1,1])
countPos([1,6,-4,-2,-7,-2])

def sumTotal(list):
    sum = 0
    for i in range (len(list)):
        sum = sum + list[i]
    return sum
sumTotal([1,2,3,4])
sumTotal([6,3,-2])

def average(list):
    sum = 0
    for i in range (len(list)):
        sum = sum + list[i]
    return (sum / len(list))
average([1,2,3,4])

def length(list):
    return len(list)
length([37,2,1,-9])
length([])

def minimum(list):
    if len(list) == 0:
        return False
    min = list[0]
    for i in range (len(list)):
        if(min > list[i]):
            min = list[i]
    return min
minimum([37,2,1,-9])
minimum([])

def maximum(list):
    if len(list) == 0:
        return False
    max = list[0]
    for i in range (len(list)):
        if(max < list[i]):
            max = list[i]
    return max
maximum([37,2,1,-9])
maximum([])

def ultAnalysis(list):
    sum = 0
    min = list[0]
    max = list[0]
    for i in range (len(list)):
        if min > list[i]:
            min = list[i]
        if max < list[i]:
            max = list[i]
        sum = sum + list[i]
    return {'sumTotal': sum, 'average': (sum / len(list)), 'minimum': min, 'maximum': max, 'length': len(list)}
ultAnalysis([37,2,1,-9])

def reverseList(list):
    for i in range (len(list) // 2):
        temp = list[i]
        list[i] = list[len(list) - 1 - i]
        list[len(list) - 1 - i] = temp
    return list

reverseList([37,2,1,-9])