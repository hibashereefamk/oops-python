#--------------------------------bank a/c----------------------
class bank_account:
    def __init__(self,balance=0):
        self.balance=balance
        print("balance",self.balance)
    def deposit(self,amount):
        self.balance +=amount
        print('amount after deposit',self.balance)
    def withdraw(self,amount):
        if amount <=self.balance:
            self.balance -=amount
            print('the amount after withdraw',self.balance)
        else:
            print('insufficient balance')
    def total_balance(self):
        return self.balance
    
acount_details=bank_account(10000)
acount_details.deposit(20000)
acount_details.withdraw(10000)
print('account balance',acount_details.total_balance())
#----------another ---------bank a/c----------------------
class BankAccount:
    def __init__(self,amount):
        self.amount=amount
        self.balance=0
    def deposit(self):
        self.balance += self.amount
        return self.balance
    def withdraw(self):
        if self.amount <=self.balance:
            self.balance -= self.amount
            return self.balance
        else:
            print('insuffient balance')
        
            
class arun(BankAccount):
    def deposit(self):
        return super().deposit()
    def withdraw(self):
        return super().withdraw()
Arun=arun(1000)
Arun = arun(1000)
print("After deposit:", Arun.deposit())
print("After withdraw:", Arun.withdraw())
