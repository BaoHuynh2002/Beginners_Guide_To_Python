class Person:
    """ An example class to hold a persons name and age"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + ' is ' + str(self.age)

    def birthday(self):
        print('Happy birthday you were', self.age)
        self.age += 1
        print('You are now', self.age)

    def calculate_pay(self, hours_worked):
        rate_of_pay = 7.50
        if self.age >= 21:
            rate_of_pay += 2.50
        return hours_worked * rate_of_pay

    def is_teenager(self):
        return self.age < 20


# Create person p1, p2, p3
p1 = Person('John', 36)
p2 = Person('Bean', 20)
p3 = Person('Chris', 16)
# Show info of person
print('# Show info of person: person.__str__()')
print(p1.__str__())
print(p2.__str__())
print(p3.__str__())
# Change person info
print('# Change person info: person.__init__(new_name, new_age)')
p1.__init__('Johnny', 40)
print(p1.__str__())
# Call function birthday in person
print('# Call function birthday in person: person.birthday()')
p2.birthday()
print(p2.__str__())
# Call function calculate_pay in person
print('# Call function calculate_pay in person: person.calculate_pay(hours)')
print(p3.name, 'worked 10 hours, was paid', p3.calculate_pay(10))
print(p1.name, 'worked 10 hours, was paid', p1.calculate_pay(10))
# Check person is teenager or not
print('# Check person is teenager or not: person.is_teenager()')
print(p1.name, 'is teenager' if p1.is_teenager() else 'is not teenager')
print(p3.name, 'is teenager' if p3.is_teenager() else 'is not teenager')
# Class attributes
print('# Class attributes')
print(Person.__name__)
print(Person.__module__)
print(Person.__doc__)
print(Person.__dict__)
# Object attributes
print('# Object attributes')
print(p1.__class__)
print(p1.__dict__)
print(p2.__dict__)
print(p3.__dict__)