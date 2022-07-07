# 1
print('#1 Integers')
x = 1
print(x)
print(type(x))
x = 100000000000000000000000000000000000000000000000000000000001
print(x)
print(type(x))
x = int('101')
print(x)
print(type(x))
# 2
print('#2 Floating point numbers')
y = 7.52
print(y)
print(type(y))
a = 1
b = '2.5'
y = float(a)
print('int value as a float:', y)
print(type(y))
y = float(b)
print('string value as a float:', y)
print(type(y))
# 3
print('#3 Complex numbers')
c1 = 1j
c2 = 2j
c3 = 1 + 2j
print('c1:', c1, ', c2:', c2)
print(type(c1))
print(c1.real)
print(c1.imag)
print('c3: ', c3)
print(type(c3))
print(c3.real)
print(c3.imag)
# 4
print('#4 Boolean values')
a = True
print(a)
a = False
print(a)
print(type(a))
b = True
b = int(b)
print(b)
b = int(b)
print(b)
print(type(b))
# 5
print('#4 Arithmetic Operators')
a = 1+2
print('1+2=', a)
a = 3-2
print('3-2=', a)
a = 3*2
print('3*2=', a)
a = 10/2
print('10/2=', a)
a = 13//3
print('13//3=', a)
a = 13%3
print('13%3=', a)
a = 3**4
print('3**4=', a)
a = (2+1j)*(3)
print('(2+1j)*(3)=', a)
# 5
print('#5 Assignment Operators')
x = 5
print('x =', x)
x += 2
print('x+=2 :', x)
x = 5
x -= 2
print('x-=2 :', x)
x = 5
x *= 2
print('x*=2 :', x)
x = 5
x /= 2
print('x/=2 :', x)
x = 5
x //= 2
print('x//=2 :', x)
x = 5
x %= 2
print('x%=2 :', x)
x = 5
x **= 2
print('x**=2 :', x)
# 6
print('#6 None Value')
a = None
print('a:', a)
print('a is None:', a is None)
print('a is not None:', a is not None)
print(type(a))
print('Set a to True')
a = True
print('a:', a)
print('a is None:', a is None)
print('a is not None:', a is not None)
print(type(a))
