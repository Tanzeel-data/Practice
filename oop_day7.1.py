class Bank:
  def __init__(self,__balance,account_holder,account_number):
    self.__balance=__balance
    self.transaction_history=[]
    self.account_holder=account_holder
    self.account_number=account_number

  def deposit (self,amount):
    self.__balance+=amount
    self.transaction_history.append(f"Deposited ${amount}")
    print(f"Deposited ${amount}. New balance: ${self.__balance}")
  
  def withdraw (self,amount):
    if amount > self.__balance:
        print("Insufficient funds.")
    else:
        self.__balance-=amount
        self.transaction_history.append(f"Withdrew ${amount}")
        print(f"Withdrew ${amount}. New balance: ${self.__balance}")

  @property
  def get_balance (self):
    return self.__balance
                            
  
  def get_transaction_history (self):
    return self.transaction_history 
  
def find_account(account_list,account_number):
  if not account_list:
    return None
  if account_list[0].account_number == account_number:
      return account_list[0]
  return find_account(account_list[1:],account_number)
                                    
def total_deposits(transaction_history):
  total=0
  for transaction in transaction_history:
    if transaction.startswith("Deposited"):
        amount = int(transaction.split("$")[1])
        total += amount
  return total


bank1 = Bank(1000,"Alice","12345")
bank1.deposit(500)
bank1.withdraw(200)
bank2 = Bank(2000,"Bob","67890")
bank2.deposit(1000)
bank2.withdraw(500)
bank2.withdraw(500)
accounts = [bank1, bank2]
account = find_account(accounts, "12345")
if account:
    print(f"Account found: {account.account_holder} with balance ${account.get_balance}")
else:
    print("Account not found.")
print(f"Total deposits for {bank1.account_holder}: ${total_deposits(bank1.get_transaction_history())}")
