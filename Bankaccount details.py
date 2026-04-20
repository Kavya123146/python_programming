#example
class Bankaccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.amount=self.amount+amount
    def withdraw(self,amount):
        self.amount=self.amount-amount
    def display(self):
        print(self.name,"Balance is:",self.balance)
ba=Bankaccount("CSE",10000)
ba.deposit(1000)
ba.withdraw(500)
ba.display()
