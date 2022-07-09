# 1
def my_function():
    # this_variables only exists and only has meaning inside my_function
    this_variables = 100
    print(this_variables)


# 2
max = 100
def print_max_plus():
    # use keyword 'global' to reference the global variable in this function
    global max
    max = max + 1
    print(max)


# 3
# both functions (outer, inner) have their own version of a title local variable
def outer():
    title = 'original title'

    def inner():
        title = 'another title'
        print('inner:', title)
    inner()
    print('outer:', title)


# use nonlocal the inner() function changes the title it will change it for both functions
def outer1():
    title = 'original title'

    def inner1():
        nonlocal title
        title = 'another title'
        print('inner1:', title)
    inner1()
    print('outer1:', title)


# 1
print('#1')
this_variables = 25
my_function()
print(this_variables)
# 2
print('#2')
print_max_plus()
print(max)
# 3
print('#3')
outer()
outer1()
