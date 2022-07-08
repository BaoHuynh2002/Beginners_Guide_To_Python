import random
# 1
print('#1')
count = 0
print('Print out the value 0-9:')
while count < 10:
    print(count, ' ', end='')  # part of the while loop
    count += 1  # also part of the while loop
print('\nFinish')  # not part of the while loop
# 2
print('#2')
print('Print out the value 0-9:')
for i in range(0, 10):
    print(i, ' ', end='')  # part of the for loop
print('\nFinish')  # not part of the for loop
print('Print out all odd numbers in range 0-10:')
for i in range(1, 10, 2):
    print(i, ' ', end='')  # part of the for loop
print('\nFinish')  # not part of the for loop
# 3
print('#3')
print('Print out the value 0-5 (use break):')
for i in range(0, 10):
    if i == 6:
        break
    print(i, ' ', end='')
print('\nFinish')
# 4
print('#4')
print('Print out all odd numbers in range 0-10 (use continue):')
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i, ' ', end='')
print('\nFinish')
# 5
print('#5')
num = 3
for i in range(0, 6):
    if i == num:
        break
    print(i, ' ', end='')
else:
    print()
    print('Else part was executed')
print()
num = 8
for j in range(0, 6):
    if j == num:
        break
    print(j, ' ', end='')
else:
    print()
    print('Else part was executed')
# 6
print('#6 Dice Roll Game')
MIN = 1
MAX = 6
roll_again = 'y'
while roll_again == 'y':
    print('Rolling the dices...')
    dice1 = random.randint(MIN, MAX)
    print('Dice 1:', dice1)
    dice2 = random.randint(MIN, MAX)
    print('Dice 2:', dice2)
    roll_again = input('Enter "y" to roll the dices again: ')
# Exercise 1
# Calculate the Factorial of a Number
# Write a program that can find the factorial of any given number. For example, find
# the factorial of the number 5 (often written as 5!) which is 1 * 2 * 3 * 4 * 5 and
# equals 120.
# The factorial is not defined for negative numbers and the factorial of Zero is 1;
# that is 0! = 1.
# Your program should take as input an integer from the user (you can reuse your
# logic from the last chapter to verify that they have entered a positive integer value
# using isnumeric()).
print('# Exercise 1 Calculate the Factorial of a Number')
x = input('Enter a positive number: ')
result = 1
while x.isnumeric() == bool(0):
    x = input('Enter a positive number: ')
if x.isnumeric():
    x = int(x)
    if x != 0:
        for i in range(1, x+1):
            result *= i
print(x, '!  =', result)
# Exercise 2
# Print All the Prime Numbers in a Range
# A Prime Number is a positive whole number, greater than 1, that has no other
# divisors except the number 1 and the number itself.
# That is, it can only be divided by itself and the number 1, for example the
# numbers 2, 3, 5 and 7 are prime numbers as they cannot be divided by any other
# whole number. However, the numbers 4 and 6 are not because they can both be
# divided by the number 2 in addition the number 6 can also be divided by the
# number 3.
# You should write a program to calculate prime number starting from 1 up to the
# value input by the user.
# If the user inputs a number below 2, print an error message.
print('# Exercise 2 Print All the Prime Numbers in a Range')
x = input('Enter a positive number (>1): ')
while x.isnumeric() == bool(0) or int(x) < 2:
    x = input('Enter a positive number: ')
print('All prime numbers from 1 to', x, ':')
x = int(x)
for i in range(2, x+1):
    for j in range(2, i):
        if (i % j) == 0:
            break
    else:
        print(i, end=', ')

