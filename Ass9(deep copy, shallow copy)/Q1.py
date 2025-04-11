import copy


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.logs = []

    def deposit(self, amount):
        self.balance += amount
        self.logs.append("Deposited " + str(amount))

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.logs.append("Withdrew " + str(amount))
        else:
            self.logs.append("Insufficient funds")


class Customer:
    def __init__(self, account):
        self.account = account


a = Account("Alice", 1000)
c = Customer(a)
c.account.deposit(200)
c.account.withdraw(150)

s = copy.copy(c)
d = copy.deepcopy(c)

c.account.deposit(100)

print("Original logs:", c.account.logs)
print("Shallow copy logs:", s.account.logs)
print("Deep copy logs:", d.account.logs)
