import random
def randInt(min='', max=''):
    if max == '' and min == '':
        num = random.random() * 100
    elif max == '':
        num = random.random() * (100 - min) + min
    elif min == '':
        num = random.random() * max
    elif max < min:
        return False
    else:
        num = random.random() * (max - min) + min
    num = round(num)
    return num
# print(randInt()) 		    # should print a random integer between 0 to 100
# print(randInt(max=50)) 	    # should print a random integer between 0 to 50
# print(randInt(min=50)) 	    # should print a random integer between 50 to 100
# print(randInt(min=50, max=500))    # should print a random integer between 50 and 500
print(randInt(min=500, max=50))
# print(randInt(max=-5))