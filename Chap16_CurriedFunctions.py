# 1
def multiply(a, b):
    return a*b


def multby(func, num):
    return lambda y: func(num, y)


# 2
def increment(num):
    return num + 1


def change_function():
    global increment
    addition = 50
    increment = lambda num: num + addition


# Exercise:
def convert(a, b):
    return a*b


def curry(func, rate):
    return lambda z: convert(rate, z)


# 1
print('#1')
double = multby(multiply, 2)
triple = multby(multiply, 3)
print(double(5))
print(triple(6))
# 2
print('#2')
print(increment(5))
change_function()
print(increment(5))
# Exercise:
print('# Exercise: ')
dollars_to_sterling = curry(convert, 0.77)
print(dollars_to_sterling(5))
euro_to_sterling = curry(convert, 0.88)
print(euro_to_sterling(15))
sterling_to_dollars = curry(convert, 1.3)
print(sterling_to_dollars(7))
sterling_to_euro = curry(convert, 1.14)
print(sterling_to_euro(9))
