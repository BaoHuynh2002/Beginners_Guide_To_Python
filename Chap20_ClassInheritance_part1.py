# Person <- Employee <- SalesPerson
class Person:
    """ An example class to hold a Person's name and age """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + " is " + str(self.age)

    def new_age(self):
        print('Your age before:', self.age)
        self.age += 1
        print('Your age now:', self.age)


class Employee(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id

    def __str__(self):
        return "ID : " + self.id + " | " + "Name: " + self.name + " | " + "Age: " + str(self.age)

    def calculate_pay(self, hours_worked):
        rate_of_pay = 7.50
        if self.age >= 21:
            rate_of_pay += 2.50
        return hours_worked * rate_of_pay


class SalesPerson(Employee):
    def __init__(self, name, age, id, region, sale_amount):
        super().__init__(name, age, id)
        self.region = region
        self.sale_amount = sale_amount

    def __str__(self):
        return super().__str__() + " | " + "Region: " + self.region + " | " + "Amount: " + str(self.sale_amount)

    def pay_on_amount(self):
        return str(self.sale_amount * 2) + "$"


# Person
print('# Person')
p = Person('John', 54)
p1 = Person('Chris', 29)
print(p)
print(p1)
print('-' * 25)
# Employee
print('# Employee')
e = Employee('Denise', 51, 'E001')
e1 = Employee(p1.name, p1.age, 'SE001')  # p1 = Person('Chris', 29)
print(e)
print(e1)
print('-' * 25)
# SalesPerson
print('# SalesPerson')
s = SalesPerson(e1.name, e1.age, e1.id, 'US', 150)
s1 = SalesPerson('Phoebe', 21, 'SE002', 'UK', 300)
print(s)
print(s1)
print('-' * 25)
# Call function new_age() _ All three class can call
print('# new_age()')
print(p)
print('> p.new_age()')
p.new_age()
print('-' * 10)
print(e1)
print('> e1.new_age()')
e1.new_age()
print('-' * 10)
print(s1)
print('> s1.new_age()')
s1.new_age()
print('-' * 25)
# Call function calculate_pay(hours_worked) _ Employee class and SalesPerson class can call
print('# calculate_pay(hours_worked)')
print('e.calculate_pay(12) =', e.calculate_pay(12))
print('s1.calculate_pay(13) =', s1.calculate_pay(13))
print('-' * 25)
# Call function pay_on_amount() _ Only SalesPerson class can call
print('# pay_on_amount()')
print('s.pay_on_amount() =', s.pay_on_amount())
print('s1.pay_on_amount() =', s1.pay_on_amount())
