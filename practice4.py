print("Welcome to ABC bank")
class Bank():
    balance=50000
    attempts=0
    max_withdraw=3
    def viewOptions(self):
        print("1.deposit")
        print("2.withdraw")
        print("3.balance")
        print("0.exit")

    def deposit(self):
        amt = int(input("enter amount to be added "))
        if (amt < 100):
            print("amount should be greater than 100")
        elif (amt % 100 != 0):
            print("the amount should be multiples of 100")
        elif (amt > 50000):
            print("the amount to be deposited should be less than 50K")
        else:
            self.balance += amt
            print("amount deposited successfully")
    def withdraw(self):
        if self.attempts>=self.max_withdraw:
            print("transaction limit reached no more withdrawls")
            return
        amt=int(input("enter amount to be withdrawn "))
        if(self.balance>500):
            if (amt < 100):
                print("amount to be withdrawn must be greater than 100")
            elif (amt % 100 != 0):
                print("the amount should be in multiples of 100")
            elif (amt > self.balance):
                print("insufficient balance")
            elif (amt > 20000):
                print("amount should not be greater than 20K")
            else:
                self.balance -= amt
                self.attempts+=1
                print("balance withdrawn successfully")
        else:
            print("insufficient balance")

    def display(self):
        print("current balance is: ",self.balance)
    def validate(self):
        for i in range(3,0,-1):
            pin = int(input("enter pin number "))
            if pin==1234:
                while True:
                    self.viewOptions()
                    n = int(input("choose an option "))
                    match n:
                        case 1:
                            self.deposit()
                        case 2:
                            self.withdraw()
                        case 3:
                            self.display()
                        case 0:
                            print("exiting...")
                            exit(0)
                        case _:
                            print("enter valid option")
            else:
                if i == 1:
                    print("card blocked")
                else:
                    print("invalid PIN number chances left ",i-1)

obj=Bank()
obj.validate()