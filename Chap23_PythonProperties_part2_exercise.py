# In this exercise you will add properties to an existing class.
# Return to the Account class that you created several chapters ago; convert the
# balance into a read only property using decorators, then verify that the following
# program functions correctly:
# private attribute syntax: _<name> or _<name>__<description>
class Account:
    """ Class Account with 3 attributes account_number, account_holder, opening_balance"""
    instance_count = 0

    @classmethod
    def increase_count(cls):
        cls.instance_count += 1

    def __init__(self, account_number, account_holder, opening_balance):
        self._account__number = account_number
        self._account__holder = account_holder
        self._opening__balance = opening_balance
        self.increase_count()

    @property
    def balance(self):
        return self._opening__balance

    @balance.getter
    def balance(self):
        return self._opening__balance

    def __str__(self):
        return "ID: " + str(self._account__number) + "\t| Name: " + self._account__holder + "\t| Balance: " \
               + str(self._opening__balance)


class CurrentAccount(Account):
    """ Subclass CurrentAccount inherits from Class Account with an overdraft_limit attribute"""
    def __init__(self, account_number, account_holder, opening_balance, overdraft_limit):
        super().__init__(account_number, account_holder, opening_balance)
        self._overdraft__limit = overdraft_limit
        Account.increase_count()

    def __str__(self):
        return super().__str__() + "\t| Limit: " + str(self._overdraft__limit)

    def withdraw(self, amount):
        if self._opening__balance <= amount:
            print('# Your balance is lower than your with-draw number.')
        else:
            self._opening__balance -= amount
            print('# With-draw {}$ successful!\n>Your balance now : {:0.2f}$'.format(amount, self._opening__balance))

    def deposit(self, amount):
        if float(amount) > 0:
            self._opening__balance += amount
            print('# Deposit {}$ successful!\n>Your balance now : {:0.2f}$'.format(amount, self._opening__balance))


class DepositAccount(Account):
    """ Subclass DepositAccount inherits from Class Account with an interest_rate attribute"""
    def __init__(self, account_number, account_holder, opening_balance, interest_rate):
        super().__init__(account_number, account_holder, opening_balance)
        self._interest__rate = interest_rate
        Account.increase_count()

    def __str__(self):
        return super().__str__() + "\t| Rate: " + str(self._interest__rate)


class InvestmentAccount(Account):
    """ Subclass InvestmentAccount inherits from Class Account with an investment_type attribute"""
    def __init__(self, account_number, account_holder, opening_balance, investment_type):
        super().__init__(account_number, account_holder, opening_balance)
        self._investment__type = investment_type
        Account.increase_count()

    def __str__(self):
        return super().__str__() + "\t| Type: " + str(self._investment__type)


acc1 = CurrentAccount('123', 'John', 10.05, 100.0)
acc2 = DepositAccount('345', 'John', 23.55, 0.5)
acc3 = acc3 = InvestmentAccount('567', 'Phoebe', 12.45, 'high risk')
print(acc1)
print(acc2)
print(acc3)
print('-'*10)
print('Number of Account instances created:', Account.instance_count)
print('-'*10)
print(acc1)
acc1.deposit(23.45)
acc1.withdraw(12.33)
print('Balance:', acc1.balance)
print('-'*10)
print(acc2)
print('Balance:', acc2.balance)
print('-'*10)
print(acc3)
print('Balance:', acc3.balance)


