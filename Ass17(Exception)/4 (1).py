
class InsufficientBalanceError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Transaction failed: Insufficient balance. Available: ₹{balance}, Requested: ₹{amount}")

def withdraw(balance, amount):
    try:
        if amount > balance:
            raise InsufficientBalanceError(balance, amount)
        else:
            balance -= amount
            print(f"Withdrawal of ₹{amount} successful. Remaining balance: ₹{balance}")
    except InsufficientBalanceError as e:
        print("Error:", e)

withdraw(5000, 3000)   # Valid
withdraw(2000, 2500)   # Invalid
