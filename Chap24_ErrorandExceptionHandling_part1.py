# The syntax for a try statement with an except clause is
# try:
# <code to monitor>
# except <type of exception to monitor for>:
# <code to call if exception is found>

# 1 2 3
def runcalc(x):
    x / 0


# 4
def my_function(x, y):
    result = x / y
    return result


# 5
def function_bang():
    print('before raise ValueError()')
    raise ValueError('Bang!')
    print('after raise ValueError()')


def function_bang1():
    print('before raise ValueError')
    raise ValueError
    print('after raise ValueError')


# 1
print('#1')
try:
    runcalc(6)
except Exception:
    print('Exception')
# 2
print('#2')
try:
    runcalc(7)
except ZeroDivisionError as exp:
    print(exp)
    print('ZeroDivisionError')
# 3
print('#3')
try:
    runcalc(6)
except ZeroDivisionError as exp:
    print(exp)
    print('ZeroDivisionError')
except IndexError as e:
    print(e)
    print('IndexError')
except Exception as exception:
    print(exception)
    print('Exception')
# 4
print('#4')
try:
    print(my_function(6, 2))
    print('>finish my_function')
except ZeroDivisionError as exp:
    print(exp)
print('Done')
print('-'*5)
try:
    print(my_function(6, 0))
    print('>finish my_function')
except ZeroDivisionError as exp:
    print(exp)
print('Done')
print('-'*5)
try:
    print(my_function(5, 0))
    print('>finish my_function')
except:
    print('Something went wrong')
print('Done')
print('-'*5)
try:
    my_function(6, 2)
except ZeroDivisionError as e:
    print(e)
else:
    print('Everything worked OK')
print('Done')
print('-'*5)
try:
    my_function(6, 0)
except ZeroDivisionError as e:
    print(e)
else:
    print('Everything worked OK')
finally:
    print('Always runs')
print('-'*5)
try:
    my_function(6, 4)
except ZeroDivisionError as e:
    print(e)
else:
    print('Everything worked OK')
finally:
    print('Always runs')
# 5
print('#5')
try:
    function_bang()
except ValueError as s:
    print(s)
print('-'*5)
try:
    function_bang1()
except ValueError:
    print('oops')
    raise
