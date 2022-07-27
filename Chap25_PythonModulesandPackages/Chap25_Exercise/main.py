# The aim of this exercise is to create a module for the classes you have been developing.
# - You should move your Account, CurrentAccount, DepositAccount and BalanceError
#   classes into a separate module (file) called accounts. Save this file into a
#   new Python package called fintech.
# - Separate out the test application from this module so that you can import the
#   classes from the package.
import Chap25_PythonModulesandPackages.Chap25_Exercise.fintech.accounts as accounts
acc1 = accounts.CurrentAccount('123', 'John', 10.05, 100.0)
acc2 = accounts.DepositAccount('345', 'John', 23.55, 0.5)
acc3 = accounts.InvestmentAccount('567', 'Phoebe', 12.45, 'high risk')
print('#1')
print(acc1)
print(acc2)
print(acc3)
print('#2')
acc1.deposit(23.45)
print('#3')
acc1.withdraw(12.33)
print('balance:', acc1.balance)
print('#4')
print('Number of Account instances created:', accounts.Account.instance_count)
print('#5')
try:
    print('balance:', acc1.balance)
    acc1.withdraw(300.00)
    print('balance:', acc1.balance)
except accounts.BalanceError as e:
    print('Handling Exception')
    print(e)
