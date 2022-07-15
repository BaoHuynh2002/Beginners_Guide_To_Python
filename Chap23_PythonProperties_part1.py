# 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'Person[' + str(self.name) + '] is ' + str(self.age)


# 2
class Person2:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return 'Person[' + str(self._name) + '] is ' + str(self._age)


# 3
class Person3:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if isinstance(new_age, int) and new_age>0 and new_age<120:
                print('OK!')
                self._age = new_age

    def get_name(self):
        return self._name

    def __str__(self):
        return 'Person[' + str(self._name) + '] is ' + str(self._age)


# 4
class Person4:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if isinstance(new_age, int) and new_age>0 and new_age<120:
                print('OK!')
                self._age = new_age

    p_age = property(fget=get_age, fset=set_age, doc="An age property")

    def get_name(self):
        return self._name

    p_name = property(fget=get_age, doc="An name property")

    def __str__(self):
        return 'Person[' + str(self._name) + '] is ' + str(self._age)


# 5
class Person5:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        """ The docstring for the age property """
        print('In age method')
        return self._age

    @property
    def name(self):
        """ The docstring for the name property """
        print('In name method')
        return self._name

    @age.setter
    def age(self, new_age):
        print('In set_age method')
        if isinstance(new_age, int) and new_age>0 and new_age<120:
                print('OK!')
                self._age = new_age

    @age.getter
    def age(self):
        print('In get_age method')
        return self._age

    @name.getter
    def name(self):
        print('In get_name method')
        return self._name

    @age.deleter
    def age(self):
        del self._age

    @name.deleter
    def name(self):
        del self._name

    def __str__(self):
        return 'Person[' + str(self._name) + '] is ' + str(self._age)


# 1
# Name and age are part of the class’s public interface it means that we can write
print('#1')
person = Person('John', 54)
person.name = 42
person.age = -1
print(person)
# How to treat age and name as being private to the object ?
# > prefixing the attribute names with an under-bar ('_')
# > look at class Person2 (#2) above
# 2
print('#2')
person = Person2('John', 54)
person.name = 42
person.age = -1
print(person)
# _name and _age is being private
# How to take(get) or write(set) _age and _name (private attributes) to the object ?
# > create function get_{name}, set_{name} in class
# > look at class Person3 (#3) above
# 3
print('#3')
person = Person3('John', 54)
person.set_age(-1)
print(person)
person.set_age(99)
print(person)
# We can create a new property and that specific methods were to be used to set and get the values of this property
# The syntax: <property_name> = property(fget=None, fset=None, fdel=None, doc=None)
# > Create property: p_age, p_name (_age, _name will be called p_age, p_name)
# > look at class Person4 (#4) above
# 4
print('#4')
person = Person4('John', 54)
print(person)
print('person.age :', person.p_age)
print('person.name :', person.p_name)
person.p_age = 21
print(person)
# Class using decorators
# > Create 2 properties: age, name (_age, _name) by using decorators
# > look at class Person5 (#5) above
# 5
print('#5')
person = Person5('Bean', 20)
print(person)
print('person.age :', person.age)
print('person.name :', person.name)
person.age = 30
print(person)


