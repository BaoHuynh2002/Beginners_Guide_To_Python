class Account:
    """ A class to hold an account with account id, name, age, type account"""
    def __init__(self, account_id, name, money, type_account):
        self.account_id = account_id
        self.name = name
        self.money = money
        self.type_account = type_account

    def __str__(self):
        s = 'Account[' + self.account_id + '] - ' + self.name + ' - ' + self.type_account + ' account =' \
            + str(self.money)
        return s

    def deposit(self, num):
        self.money += num
        print('Deposit successful! \n>[Account -', self.account_id, '] Your balance now:', self.money)

    def withdraw(self, num):
        if self.money >= num:
            self.money -= num
            print('Withdraw successful! \n>[Account -', self.account_id, '] Your balance now:', self.money)
        else:
            print('Withdraw unsuccessful!\n>[Account -', self.account_id, '] Your balance is not enough to withdraw.')

    def get_balance(self):
        return self.money


acc1 = Account('123', 'John', 10.05, 'current')
acc2 = Account('345', 'Johnny', 23.55, 'savings')
acc3 = Account('567', 'Phoebe', 12.45, 'investment')
print(acc1)
print(acc2)
print(acc3)
print('-'*10)
acc1.deposit(23.45)
print('-'*10)
acc1.withdraw(12.33)
print('-'*10)
print('Balance of [Account - ', acc1.account_id, '] :', acc1.get_balance())