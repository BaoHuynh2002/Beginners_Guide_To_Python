# This exercise involves adding error handling support to the CurrentAccount class.
# 1- In the CurrentAccount class it should not be possible to withdraw or deposit a negative amount.
# 2- Define an exception/error class called AmountError.
#       The AmountError should take the account involved and an error message as parameters.
# 3- Next update the deposit() and withdraw() methods on the Account and CurrentAccount class
#    to raise an AmountError if the amount supplied is negative.
# 4- Next modify the class such that if an attempt is made to withdraw money which
#    will take the balance below the over draft limit threshold an Error is raised.
#           The Error should be a BalanceError that you define yourself.
#           The BalanceError exception should hold information on the account that generated the error.
class AmountError(Exception):
    """ In the CurrentAccount class it should not be possible to withdraw or deposit a negative amount """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Cant withdraw / deposit a negative amount ({:0.2f}).".format(self.value)


class BalanceError(Exception):
    """ In the CurrentAccount class balance should not be under 5$ or negative amount"""
    def __init__(self, balance, value):
        self.balance = balance
        self.value = value

    def __str__(self):
        s1 = "Your balance [{:0.2f}$] is not enough to withdraw this amount ({:0.2f})."
        s2 = "Your balance should not be under 5$ ({:0.2f}$ left if withdraw {:0.2f}$)."
        if (self.balance-self.value) < 0:
            return s1.format(self.balance, self.value)
        elif (self.balance-self.value) < 5:
            return s2.format(self.balance-self.value, self.value)


class Account:
    """ Class Account with 3 attributes account_number, account_holder, opening_balance"""
    def __init__(self, account_number, account_holder, opening_balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.opening_balance = opening_balance

    def __str__(self):
        return "ID: " + str(self.account_number) + "\t| Name: " + self.account_holder + "\t| Balance: " \
               + str(self.opening_balance)


class CurrentAccount(Account):
    """ Subclass CurrentAccount inherits from Class Account with an overdraft_limit attribute"""
    def __init__(self, account_number, account_holder, opening_balance, overdraft_limit):
        super().__init__(account_number, account_holder, opening_balance)
        self.overdraft_limit = overdraft_limit

    def __str__(self):
        return super().__str__() + "\t| Limit: " + str(self.overdraft_limit)

    def with_draw(self, amount):
        if amount < 0:
            raise AmountError(amount)
        else:
            if self.opening_balance < amount+5:
                raise BalanceError(self.opening_balance, amount)
            else:
                self.opening_balance -= amount
                print('# With-draw {}$ successful!\n>Your balance now : {:0.2f}$'.format(amount, self.opening_balance))

    def deposit(self, amount):
        if amount < 0:
            raise AmountError(amount)
        else:
            if float(amount) > 0:
                self.opening_balance += amount
                print('# Deposit {}$ successful!\n>Your balance now : {:0.2f}$'.format(amount, self.opening_balance))


acc1 = CurrentAccount('123', 'John', 10.05, 100.0)
print(acc1)

try:
    acc1.with_draw(5.25)
except AmountError as s:
    print('#', s)
except BalanceError as s1:
    print('#', s1)

try:
    acc1.deposit(-10.05)
except AmountError as s:
    print('#', s)
except BalanceError as s1:
    print('#', s1)

try:
    acc1.with_draw(4.23)
except AmountError as s:
    print('#', s)
except BalanceError as s1:
    print('#', s1)

try:
    acc1.deposit(10.32)
except AmountError as s:
    print('#', s)
except BalanceError as s1:
    print('#', s1)

