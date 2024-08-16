class Account:
    def __init__(self, bal, acc):  # constructor
        self.balance = bal
        self.account_no = acc

    # debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs", amount, "was debited")
        print("total balance =", self.get_balance())

    # credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance =", self.get_balance())

    # get_balance method
    def get_balance(self):
        return self.balance



  


acc1=Account(10000,12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(20000)


  