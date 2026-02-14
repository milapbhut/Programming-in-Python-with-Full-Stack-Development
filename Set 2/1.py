class customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

class bank:
    def create_account(self, customer, account):
        print("Account created")
        print(f"Customer Name: {customer.name}")
        print(f"Account Number: {account.account_number}")
        print(f"Balance: {account.balance}")


customer1 = customer("John Doe", 30)
account1 = account("123456789", 1000)

bank1 = bank()
bank1.create_account(customer1, account1)