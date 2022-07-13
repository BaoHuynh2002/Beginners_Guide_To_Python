# Operator                  Expression          Method
# Less than                 q1 < q2             __lt__(q1, q2)
# Less than or equal to     q1 <= q2            __le__(q1, q2)
# Equal to                  q1 == q2            __eq__(q1, q2)
# Not Equal to              q1 != q2            __ne__(q1, q2)
# Greater than              q1 > q2             __gt__(q1, q2)
# Greater than or equal to  q1 >= q2            __ge__(q1, q2)
# ----------------------------------------------------------------
# AND                       q1 & q2             __and__(q1, q2)
# OR                        q1 | q2             __or__(q1, q2)
# XOR                       q1 ^ q2             __xor__(q1, q2)
# NOT                       *q1                 __invert__()
# ----------------------------------------------------------------

class Quantity:
    def __init__(self, value=0):
        self.value = value

    def __str__(self):
        return 'Quantity[' + str(self.value) + ']'

    def __add__(self, other):
        new_value = self.value + other.value
        return Quantity(new_value)

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value


q1 = Quantity(5)
q2 = Quantity(10)
print('q1 =', q1, ',q2 =', q2)
q3 = q1 + q2
print('q3 =', q3)
print('q1 < q2: ', q1 < q2)
print('q3 > q2: ', q3 > q2)
print('q3 == q1: ', q3 == q1)
print('q3 >= q1: ', q3 >= q1)