# Defining an Custom Exception
# 1
class InvalidAgeException(Exception):
    """ Valid Ages must be between 0 and 120 """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Set Age [{}] is not available.".format(self.value)


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return 'Person[' + str(self._name) + '] is ' + str(self._age)

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @name.getter
    def name(self):
        return self._name

    @age.getter
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, int) & (value > 0 & value < 120):
            self._age = value
        else:
            raise InvalidAgeException(value)


# 2
class DivideByYWhenZeroException(Exception):
    """ Sample Exception class"""


def divide(x, y):
    try:
        result = x /y
    except Exception as e:
        raise DivideByYWhenZeroException from e


def main():
    divide(6, 0)


# 1
print('#1')
try:
    p = Person('Adam', 21)
    p.age = -1
    print(p)
except InvalidAgeException:
    print('Error')

try:
    p = Person('Chris', 25)
    p.age = -1
    print(p)
except InvalidAgeException as s:
    print(s)
# 1
print('#2  Chaining Exceptions')
main()

