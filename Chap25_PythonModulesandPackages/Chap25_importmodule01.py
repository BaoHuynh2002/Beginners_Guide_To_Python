import Chap25_module01

print('#1')
Chap25_module01.printer('OK')
print('#2')
Chap25_module01.printer(Chap25_module01.default_shape)
print('#3')
newshape = Chap25_module01.Shape('Circle')
Chap25_module01.printer(newshape)


# We can import a module within a function
def my_func():
    from Chap25_module01 import printer, default_shape as df_shape
    printer(df_shape)


print('#4')
my_func()