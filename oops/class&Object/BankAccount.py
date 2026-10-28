class BankAccount:

    account_counter = 1000

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

        BankAccount.account_counter += 1
        self.account_number = BankAccount.account_counter

    def deposit(self, amount):
        self.balance += amount
        print(amount, "deposited successfully")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "withdrawn successfully")
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

    def transfer(self, amount, other_account):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print(amount, "transferred successfully")
        else:
            print("Insufficient balance for transfer")


# Creating two accounts
account1 = BankAccount("Tejas")
account2 = BankAccount("Rahul")

# Deposit
account1.deposit(5000)
account2.deposit(3000)

# Withdraw
account1.withdraw(1000)

# Transfer
account1.transfer(2000, account2)

# Display balances
print("\nAccount 1:")
account1.display_balance()

print("\nAccount 2:")
account2.display_balance()