# Operator              Expression      Method
# Addition              q1 + q2         __add__(self, q2)
# Subtraction           q1 – q2         __sub__(self, q2)
# Multiplication        q1 * q2         __mul__(self, q2)
# Power                 q1 ** q2        __pow__(self, q2)
# Division              q1 / q2         __truediv__(self, q2)
# Floor Division        q1 // q2        __floordiv__(self, q2)
# Modulo(Remainder)     q1 % q2         __mod__(self, q2)
# Bitwise Left Shift    q1 << q2        __lshift__(self, q2)
# Bitwise Right Shift   q1 >> q2        __rshift__(self, q2)
# ------------------------------------------------------------
# Example:
class Quantity:
    def __init__(self, value=0):
        self.value = value

    def __str__(self):
        return 'Quantity[' + str(self.value) + ']'

    def __add__(self, other):
        new_value = self.value + other.value
        return Quantity(new_value)

    def __sub__(self, other):
        new_value = self.value - other.value
        return Quantity(new_value)

    def __mul__(self, other):
        new_value = self.value * other.value
        return Quantity(new_value)

    def __pow__(self, other):
        new_value = self.value ** other.value
        return Quantity(new_value)

    def __truediv__(self, other):
        new_value = self.value / other.value
        return Quantity(new_value)

    def __floordiv__(self, other):
        new_value = self.value // other.value
        return Quantity(new_value)


q1 = Quantity(100)
q2 = Quantity(10)
q3 = Quantity()
q4 = Quantity(2)
print('Quantity 1:', q1)
print('Quantity 2:', q2)
print('Quantity 3:', q3)
print('Quantity 4:', q4)
q3 = q1 - q2
print('q3 = q1 - q2:', q3)
q3 = q1 + q2
print('q3 = q1 + q2:', q3)
q3 = q1 * q2
print('q3 = q1 * q2:', q3)
q3 = q2 ** q4
print('q3 = q2 ** q4:', q3)
q3 = q1 / q2
print('q3 = q1 / q2:', q3)
q3 = q2 // q4
print('q3 = q2 // q4:', q3)
