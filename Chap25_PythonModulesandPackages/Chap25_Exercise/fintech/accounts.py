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
        if amount < 0:
            raise AmountError(amount)
        else:
            if self._opening__balance < amount + 5:
                raise BalanceError(self._opening__balance, amount)
            else:
                self._opening__balance -= amount
                print('# With-draw {}$ successful!\n>Your balance now : {:0.2f}$'.format(amount, self._opening__balance))

    def deposit(self, amount):
        if amount < 0:
            raise AmountError(amount)
        else:
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


