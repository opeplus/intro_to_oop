class Account:
    def __init__(self):
        self.balance = 10000
        self.__interest_rate = 5
        self.__id_number = 'DG57895'
        print('starting balance is: ', self.balance)
    def get_interest_rate(self):
        return self.__interest_rate
    def get_id_number(self):
        return self.__id_number

    def set_id_number(self,new_id_number):
        self.__id_number = new_id_number

    def deposit(self, amount):
        self.balance = amount + self.balance
        print('the new balance is: ', self.balance)


    def withdraw(self, amount):
            self.balance = self.balance - amount
            print('The new balance is:', self. balance)
