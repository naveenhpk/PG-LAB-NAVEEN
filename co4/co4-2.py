class Bank:
    def __init__(self):
        self.bal=0
    def create(self) :
        print("enter The Details")
        self.no=int(input("enter the account Number"))
        self.name=input("enter the name")
        self.type=input("Entr the account type")
    def deposit(self):
        self.amount=int(input("enter the amount to deposit"))
        self.bal=self.bal+self.amount
        print("BALANCE",self.bal)
    def withdraw(self):
        self.amount=int(input("enter the amount to withdraw"))
        self.bal=self.bal-self.amount
        print("BALANCE",self.bal)
    def display(self):
        print("ACCOUNT NUMBER:",self.no)
        print("ACCOUNT HOLDER NAME:",self.name)
        print("ACCOUNT TYPE:",self.type)
        print("ACCOUNT BALANCE:",self.bal)

B=Bank()
B.create()
x=1
while x!=0:
    print("MENU")
    x=int((input("1.DEPOSIT 2.WITHDRAW 3.BALANCE")))
    if x==1:
        B.deposit()
    elif x==2:
        B.withdraw()
    elif x==3:
        B.display()
    else:
        print("invalid selection")