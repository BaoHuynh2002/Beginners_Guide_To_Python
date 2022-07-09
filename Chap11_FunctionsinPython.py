# 1
def print_my_msg_allupper(msg):
    print(str(msg).upper())


# 2
def perimeter_of_square(n):
    return 4*n


def swap(a, b):
    return b, a


# 3
def get_integer_input(message):
    """
    This function will display the message to the user
    and request that they input an integer.
    If the user enters something that is not a number
    then the input will be rejected
    and an error message will be displayed.
    The user will then be asked to try again."""
    value_as_string = input(message)
    while not value_as_string.isnumeric():
        print('The input must be an integer')
        value_as_string = input(message)
    return int(value_as_string)


# 4
def default_function(name, message='You are handsome.'):
    print('Hi', name, ',', message)


# 5
def greeter(*args):
    for name in args:
        print('Welcome', name)


# 6
def my_function(**kwargs):
    for key in kwargs.keys():
        print('key:', key, '\t value:', kwargs[key])


# 1
print('#1')
print_my_msg_allupper('hello')
print_my_msg_allupper('worD')
# 2
print('#2')
print('perimeter of square (5): ', perimeter_of_square(5))
print('perimeter of square (8): ', perimeter_of_square(8))
a = 5
b = 7
print('before: a =', a, ', b =', b)
a, b = swap(a, b)
print('after swap: a =', a, ', b =', b)
# 3
print('#3')
x = get_integer_input('Enter your age: ')
print('Your age:', x)
print('Explain function:')
print(get_integer_input.__doc__)
# 4
print('#4')
default_function('Bao')
default_function('Bean', 'Are you happy ?')
# 5
print('#5')
greeter('Bao', 'Ben', 'Bin', 'Tien', 'Hoang')
# 6
print('#6')
my_function(a=1, b=2, c=3, d=4)
print('-'*10)
my_function(Seasons_of_A_Year='Spring, Summer, Autumn, Winter', Month_with_less_than_30days='February')
# 7
print('#7')
func1 = lambda x: x*x
func2 = lambda x, y: (x+y)/2
print(func1(3))
print(func1(4))
print(func2(2, 4))
print(func2(4, 4))