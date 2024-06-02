from account import Account
class SavingsAccount(Account):
    def __init__(self):
        Account.__init__(self)
# method of polymorphism include the following inheritance)
#overriding(writing a method over another method:that method now has numerous forms)
#method overloading(a class having numerous methods but diff parameters)

    def withdraw(self, amount):
        if amount < 5000:
            super().withdraw(amount)
        else:
            print('you can not withdraw above your limit')
savings = SavingsAccount()
savings.withdraw(8000)
#benefit of encapsulation is read and write
