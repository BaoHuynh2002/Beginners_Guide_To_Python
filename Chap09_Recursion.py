# 1
# the factorial of the number 5
# (written as 5!)
# function:
def factorial(n):
    if n == 1:  # The termination condition
        print(1)
        return 1  # The base case
    else:
        res = n * factorial(n-1)  # The recursive call
        print('res =', n, '* factorial(', n-1, ')')
        return res


def checkPrimeRecursion(numb, divisors=None):
    if divisors is None:
        divisors = numb - 1
    while divisors >= 2:
        if numb % divisors == 0:
            # if we find the divisor then return false because it is not prime
            return False
        else:
            return checkPrimeRecursion(numb, divisors-1)
    else:
        # if we reach here return true because we did not find any
        # divisors of the given number
        return True


def pascals_traingle_row(num_of_row):
    if num_of_row == 0:
        return []  # Null List
    elif num_of_row == 1:
        return [1]
    else:
        new_row = [1]  # First value of row is 1
        last_row = pascals_traingle_row(num_of_row-1)
        for i in range(len(last_row)-1):
            new_row.append(last_row[i]+last_row[i+1])
        new_row += [1]  # Last value of row is 1
    return new_row


def pascals_traingle(row):
    for i in range(1, row+1):
        print(pascals_traingle_row(i))
    return 'Done!'


print('#1')
print('5! = ', factorial(5))
print('#2')
numb = input('Enter a number (>1): ')
while numb.isnumeric() == bool(0) or int(numb) < 2:
    numb = input('Enter a number (>1): ')
is_Prime = checkPrimeRecursion(int(numb))
print('Your number "', numb, '" is', 'a prime number.' if is_Prime else 'not a prime number.')
print('#3')
row = input('Enter a number (>0): ')
while row.isnumeric() == bool(0) or int(row) <= 0:
    row = input('Enter a number (>0): ')
print('Pascal Traingle with', int(row), 'row(s).')
print(pascals_traingle(int(row)))
