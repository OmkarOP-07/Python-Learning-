import copy

class JointAccount:
    def __init__(self, name1, name2, balance):
        self.holder1 = name1
        self.holder2 = name2
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

account = JointAccount("Husband", "Wife", 1000)
husband = Customer(account)
wife = Customer(account)
husband.account.deposit(300)
wife.account.withdraw(150)
shallow_copy = copy.copy(husband)
deep_copy = copy.deepcopy(wife)
husband.account.deposit(200)
print("Husband logs:", husband.account.logs)
print("Wife logs:", wife.account.logs)
print("Shallow copy logs:", shallow_copy.account.logs)
print("Deep copy logs:", deep_copy.account.logs)
