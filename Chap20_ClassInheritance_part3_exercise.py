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
        if self.opening_balance <= amount:
            print('# Your balance is lower than your with-draw number.')
        else:
            self.opening_balance -= amount
            print('# With-draw {}$ successful!\n>Your balance now : {:0.2f}$'.format(amount, self.opening_balance))

    def deposit(self, amount):
        if float(amount) > 0:
            self.opening_balance += amount
            print('# Deposit {}$ successful!\n>Your balance now : {:0.2f}$'.format(amount, self.opening_balance))


class DepositAccount(Account):
    """ Subclass DepositAccount inherits from Class Account with an interest_rate attribute"""
    def __init__(self, account_number, account_holder, opening_balance, interest_rate):
        super().__init__(account_number, account_holder, opening_balance)
        self.interest_rate = interest_rate

    def __str__(self):
        return super().__str__() + "\t| Rate: " + str(self.interest_rate)


class InvestmentAccount(Account):
    """ Subclass InvestmentAccount inherits from Class Account with an investment_type attribute"""
    def __init__(self, account_number, account_holder, opening_balance, investment_type):
        super().__init__(account_number, account_holder, opening_balance)
        self.investment_type = investment_type

    def __str__(self):
        return super().__str__() + "\t| Type: " + str(self.investment_type)


acc1 = CurrentAccount('123', 'John', 10.05, 100.0)
print(acc1)
acc1.with_draw(5.25)
acc1.deposit(10.05)
acc2 = DepositAccount('345', 'John', 23.55, 0.5)
acc3 = InvestmentAccount('567', 'Phoebe', 12.45, 'high risk')
print(acc2)
print(acc3)
