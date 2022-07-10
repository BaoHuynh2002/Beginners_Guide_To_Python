# 1
def get_some_other_msg():
    return 'Some other message!!!'


# 2
def add(x, y):
    return x+y
def sub(x, y):
    return x-y
def apply(x, y, function):
    result = function(x, y)
    return result


# 3
def make_checker(s):
    if s == 'even':
        return lambda n: n % 2 == 0
    elif s == 'positive':
        return lambda n: n >= 0
    elif s == 'negative':
        return lambda n: n < 0
    else:
        raise ValueError('Unknown request')


# 4
def make_function():
    def add(x, y):
        return x+y
    return add


# Exercise:
def double(x):
    return x*x
def triple(x):
    return x*x*x
def square_root(x):
    return int(x ** 0.5)
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, int(x ** 0.5) + 1):
            if x % n == 0:
                return False
        return True
def is_integer(x):
    if str(x).isalpha():
        return False
    return True
def is_letter(x):
    return str(x).isalpha()
def my_higher_order_function(x, function):
    return function(x)


# 1
print('#1')
get_msg = get_some_other_msg
msg = get_some_other_msg()
print(get_msg())
print(get_some_other_msg())
print(msg)
# 2
print('#2')
result_0 = apply(5, 6, add)
result_1 = apply(7, 4, sub)
print('Result 0: {}'.format(result_0))
print('Result 1: {}'.format(result_1))
# 3
print('#3')
func_1 = make_checker('even')
func_2 = make_checker('positive')
func_3 = make_checker('negative')
print(func_1(99))
print(func_2(99))
print(func_3(99))
# 4
print('#4')
func_4 = make_function()
print(func_4(3, 7))
# Exercise:
print('# Exercise:')
print(my_higher_order_function(2, double))
print(my_higher_order_function(2, triple))
print(my_higher_order_function(16, square_root))
print(my_higher_order_function(2, is_prime))
print(my_higher_order_function(4, is_prime))
print(my_higher_order_function('2', is_integer))
print(my_higher_order_function('A', is_integer))
print(my_higher_order_function('A', is_letter))
print(my_higher_order_function('1', is_letter))
