import random
class Bank:
    users = []
    def __init__(self):
        pass
    def addUser(self, user):
        self.users.append(user)
    def getUserByAccountNumber(self, accountNumber):
        for user in self.users:
            if user.accountNumber == accountNumber:
                return user
        return False
    def getUserByUsername(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return False

class BankUser:
    def __init__(self, username, pin):
        self.username = username
        self.accountNumber = random.randint(100000, 999999)
        self.pin = pin
        self.balance = 0
    def deposit(self, amount, pin):
        if pin == self.pin:
            if amount > 0:
                self.balance += amount
                print(f"You have successfully deposited {amount}. New balance is {self.balance}")
            else:
                print("Enter a valid amount")
        else:
            print("Wrong pin")
    def withdraw(self, amount, pin):
        if pin == self.pin:
            if amount > 0:
                if amount > self.balance:
                    print(f"Insufficient balance. Your balance is {self.balance}")
                else:
                    self.balance -= amount
                    print(f"You have successfully withdrawn {amount}. New balance is {self.balance}")
            else:
                print("Enter a valid amount")
        else:
            print("Wrong pin")
    def transfer(self, amount, pin, accountNumber, bank):
        receiver = bank.getUserByAccountNumber(accountNumber)
        if not receiver:
            print("Receiver Not found")
            return
        if pin == self.pin:
            if amount > 0:
                if amount > self.balance:
                    print(f"Insufficient balance. Your balance is {self.balance}")
                else:
                    self.balance -= amount
                    receiver.balance += amount
                    print(f"You have successfully transferred {amount} to {receiver.username}. New balance is {self.balance}")
            else:
                print("Enter a valid amount")
        else:
            print("Wrong pin")


bank = Bank()

while True:
    userName = input("Register Users. Enter Username. Enter q to exit: ")
    if userName == "q":
        break
    pin = int(input("Enter pin: "))
    newUser = BankUser(userName, pin)
    bank.addUser(newUser)

while True:
    userName = input("Enter your Username: ")
    user = bank.getUserByUsername(userName)
    if not user:
        print("Wrong credentials")
        continue
    print("1. Deposit\n2.Withdraw\n3.Transfer")
    choice = input("Enter choice: ")

    if choice == "1":
        amount = int(input("Enter Amount: "))
        pin = int(input("Enter pin: "))
        user.deposit(amount, pin)