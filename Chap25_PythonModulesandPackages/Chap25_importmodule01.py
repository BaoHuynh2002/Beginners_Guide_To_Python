import Chap25_module01

print('#1')
Chap25_module01.printer('OK')
print('#2')
Chap25_module01.printer(Chap25_module01.default_shape)
print('#3')
newshape = Chap25_module01.Shape('Circle')
Chap25_module01.printer(newshape)