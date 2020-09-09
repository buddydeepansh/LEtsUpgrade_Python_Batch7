# program for account balance
class Account():
    def __init__(self,name,balance):
        self.name= name
        self.balance= balance

    def deposit(self):
        p = int(input("Enter amount to deposit: "))
        if p >= 0:
            self.balance += p
            print("Your account balance is: ", self.balance)
        else:
            print("Enter a valid amount!!!")

    def withdraw(self):
        p = int(input("Enter the amount you want to withdraw: "))
        if p < 0:
            print("Enter a valid amount!!!")
        elif p < self.balance:
            print("Withdrwa succesfull of amount: ",p)
            self.balance -= p
            print("Remaining balance is: ",self.balance)
        else:
            print("You donot have sufficient funds")


obj = Account("Deepansh",3000)
obj.deposit()
obj.withdraw()

# program for cone's volume and surface area
import math
class Cone():
    def __init__(self,r,h):
        self.r=r
        self.h=h

    def volume(self):
        v= 3.14*(self.r ** 2)*(self.h)/3
        print("Volume is: ",v)

    def area(self):
        a= 3.14*self.r*(self.r+(math.sqrt((self.h **2)+(self.r **2))))
        print("Surface area is: ",a)

c = Cone(5,2)
c.volume()
c.area()