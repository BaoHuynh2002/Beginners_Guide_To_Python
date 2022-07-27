from Chap25_module01 import *
# import everything from Chap25_module01.py

print('#1')
printer(default_shape)
print('#2')
printer(Shape('Circle'))
print('#3')
newshape = Shape('Square')
printer(newshape)

from Chap25_module01 import Shape,printer
# import only Shape class and printer function in Chap25_module01.py

print('#4')
newshape1 = Shape('Oval')
printer(newshape1)

import Chap25_module01 as Module01
# We call Chap25_module01 by Module01

print('#5')
printer(Module01.default_shape)
print('#6')
printer(Module01.Shape('Circle'))
print('#7')
newshape2 = Module01.Shape('Square')
printer(newshape2)

from Chap25_module01 import Shape, printer as printerinmodule01, default_shape as defaultshapeinmodule01

print('#8')
newshape1 = Shape('Oval')
printerinmodule01(newshape1)
print('#9')
printerinmodule01(defaultshapeinmodule01)