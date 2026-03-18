class BankAccount:

    # Constructor
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   # private variable

    # Getter method
    def get_balance(self):
        return self.__balance

    # Setter method
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative")

    # Method to display info
    def display(self):
        print("Account Holder:", self.name)
        print("Balance:", self.__balance)


# Creating object
account1 = BankAccount("Ali", 5000)

# Using getter
print("Current Balance:", account1.get_balance())

# Using setter
account1.set_balance(8000)

# Display updated details
account1.display()