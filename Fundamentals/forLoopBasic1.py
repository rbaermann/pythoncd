def basic():
    for i in range (151):
        print(i)

basic()

def multiplesOfFive():
    for i in range (5, 1001, 5):
        print(i)

multiplesOfFive()

def dojoWay():
    for i in range (1, 101):
        if(i % 10 == 0):
            print('Coding Dojo')
        elif(i % 5 == 0):
            print('Coding')
        else:
            print(i)

dojoWay()

def thatSuckersHuge():
    sum = 0
    for i in range (500001):
        if(i % 2 != 0):
            sum = sum + i
    print(sum)

thatSuckersHuge()

def countdownByFour():
    for i in range (2018, 0, -4):
        print(i)

countdownByFour()

def flexibleCounter(lowNum, highNum, mult):
    if(lowNum < 0):
        x = lowNum * mult
    else:
        x = 0
    for i in range (x, highNum + 1, mult):
        if(i >= lowNum):
            print(i)
            

flexibleCounter(-5, 9, 3)
