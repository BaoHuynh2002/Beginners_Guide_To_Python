# 1
print('#1')
print(3 == 3)
print(3 != 3)
print(3 < 5)
print(5 > 3)
print(5 <= 6)
print(5 >= 4)
print((3 < 4) and (5 > 4))
print((3 < 4) or (3 > 4))
print(not 3 < 2)
# 2
print('#2')
num1 = -5
if num1 < 0:
    print(num1, 'is negative')
num = int(input('Enter a number: '))
if num < 0:
    print('Its negative')
else:
    print('Its not negative')
# 3
print('#3')
num = int(input("Enter a number: "))
if num == 0:
    print("Its not negative or positive")
elif num < 0:
    print('Its negative')
else:
    print('Its positive')
# 4
print('#4')
a = 5
b = 6
if a != b:
    if a > b:
        print('a>b')
    else:
        print('a<b')
else:
    print('a=b')
compare_ab = ('a!=b' if a != b else 'a==b')
print(compare_ab)
if 1:
    print('True')
if '123':
    print('True')
# Exercise : Check Input Is Positive or Negative
x = input('Enter a number: ')
x = int(x)
if x == 0:
    print(x, 'is zero')
elif x > 0:
    print(x, 'is Positive')
else:
    print(x, 'is Negative')
