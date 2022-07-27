

print('#1')
from Package1 import *
print('#2')
from Package2 import *
print('#3')
import Package1.Module1_1
import Package1.Module1_2

# Su dung __all__ se khong goi duoc nhu Package1

import Package2.Module2_1
import Package2.Module2_2