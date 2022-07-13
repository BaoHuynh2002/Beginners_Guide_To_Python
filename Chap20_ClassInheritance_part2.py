# a class can inherit from one or more other classes (many object-oriented languages limit inheritance to a single
# class such as Java and C#)

# 1
class Car:
    def move(self):
        print('Car - move()')


class Toy:
    def move(self):
        print('Toy - move()')


class ToyCar(Car, Toy):
    """ A Toy Car """


class ToyCar1(Toy, Car):
    """ A Toy Car 1"""


# 2
class A:
    def __str__(self):
        return 'A'

    def print_info(self):
        print('A')


class B:
    def __str__(self):
        return 'B'


class C:
    def __str__(self):
        return 'C'

    def get_data(self):
        return 'CData'


class D:
    def __str__(self):
        return 'D'

    def print_info(self):
        print('D')


class E:
    def __str__(self):
        return 'E'

    def print_info(self):
        print('E')


class F(C, D, E):
    def __str__(self):
        return super().__str__() + 'F'

    def get_data(self):
        return super().get_data() + 'FData'

    def print_info(self):
        print('F' + self.get_data())


class G(C, D, E):
    def __str__(self):
        return super().__str__() + 'G'

    def get_data(self):
        return super().get_data() + 'GData'


class H(F, G):
    def __str__(self):
        return super().__str__() + 'H'

    def print_info(self):
        print('H' + self.get_data())


class J(H):
    def __str__(self):
        return super().__str__() + 'J'


class I(A, J):
    def __str__(self):
        return super().__str__() + 'I'


class X(J, H, B):
    def __str__(self):
        return super().__str__() + 'X'


# 1
print('#1')
tc = ToyCar()
ct = ToyCar1()
tc.move()
ct.move()
# 2
print('#2')
x = X()
print(x)
# X(J, H, B) '1
# J(H) '2
# H(F, G)  '3
# F(C, D, E)  '4
# => '1 -> _X -> J
#    '2 -> _JX -> H
#    '3 -> _HJX -> F and G (both have C first of father's class)
#    '4 -> _GFHJX -> C
#    '5 -> CGFHJX = x
