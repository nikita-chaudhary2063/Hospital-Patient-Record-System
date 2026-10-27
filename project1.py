'''
Nepal Payment System
'''

class Esewa:
    def __init__(self,amount):
        self.amount=amount

    def pay(self):
        print("Paid through Esewa!")

class Khalti:
    def __init__(self,amount):
       self.amount=amount

    def pay(self):
        print("Paid through Khalti!")

class BankTransfer:
    def __init__(self,amount):
        self.amount=amount

    def pay(self):
        print("Paid through Bank!")

class CashPayment:
    def __init__(self,amount):
        self.amount=amount

    def pay(self):
        print("Paid through Cash!")

esewa1=Esewa(5000)
khalti1=Khalti(7000)
bank1=BankTransfer(8000)
cash1=CashPayment(2000)

payments=[esewa1,khalti1,bank1,cash1]
for paid in payments:
    paid.pay()


        

