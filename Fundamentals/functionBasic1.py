#1
def a():
    return 5
print(a())

# prediction: 5
# correct: 5

#2
def a():
    return 5
print(a()+a())

# prediction: 10
# correct: 10

#3
def a():
    return 5
    return 10
print(a())

# prediction: 5
# correct: 5

#4
def a():
    return 5
    print(10)
print(a())

# prediction: 5
# correct: 5

#5
def a():
    print(5)
x = a()
print(x)

# prediction: 5
# correct: 5

#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))

# prediction: 3,5,8
# correct: 3,5,error

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))

 # prediction: 25
 # correct: 25

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())


# prediction: 100, 10
# correct: 100, 10

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

# prediction: 7, 14, 21
# correct: 7, 14, 21

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))

# prediction: 8
# correct: 8

#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

# prediction: 500, 300, 500
# correct: 500, 300, 500

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

# prediction: 500, 300, 300, 500
# correct: 500, 300, 300, 500

#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

# prediction: 500, 300, 300
# correct: 500, 300, 300

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

# prediction: 1, 3, 2
# correct: 1, 3, 2

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

# prediction: 
# correct: 