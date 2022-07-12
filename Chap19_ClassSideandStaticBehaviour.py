# 1
# The variable instance_count is not part of an individual object, rather it is
# part of the class and all instances of the class can access that shared variable by
# prefixing it with the class name
class EmployeeA:
    """ An example class to hold an Employee name and age"""
    instance_count = 0

    def __init__(self, name, age):
        EmployeeA.instance_count += 1
        self.name = name
        self.age = age


# 2
# The instance_count variable is accessed via the cls parameter passed into
# the increment_instance_count method
class EmployeeB:
    """ An example class to hold an Employee name and age"""
    instance_count = 0

    @classmethod
    def increment_instance_count(cls):
        cls.instance_count += 1

    def __init__(self, name, age):
        EmployeeB.increment_instance_count()
        self.name = name
        self.age = age


# 3
class EmployeeC:
    @staticmethod
    def static_function():
        print('This is employeeC class')


# Exercise:
class Account:
    """ An example class to hold an Account name and age"""
    instance_count = 0

    @classmethod
    def increment_instance_count(cls):
        cls.instance_count += 1

    @staticmethod
    def static_function():
        print('New Account is created!')

    def __init__(self, name, age):
        Account.increment_instance_count()
        Account.static_function()
        self.name = name
        self.age = age


# 1
print('#1')
p1 = EmployeeA('Jason', 36)
p2 = EmployeeA('Carol', 21)
p3 = EmployeeA('James', 19)
p4 = EmployeeA('Tom', 31)
print(EmployeeA.instance_count)
# 2
print('#2')
p5 = EmployeeB('Jason', 36)
p6 = EmployeeB('Carol', 21)
p7 = EmployeeB('James', 19)
p8 = EmployeeB('Tom', 31)
p9 = EmployeeB('Bean', 20)
print(EmployeeB.instance_count)
# 3
print('#3')
EmployeeC.static_function()
# Exercise
print('#Exercise')
e1 = Account('Jason', 36)
e2 = Account('Carol', 19)
e3 = Account('Tom', 26)
print('Number of Account instances created:', Account.instance_count)
