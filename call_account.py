from account import Account 
from decimal import Decimal 

account1 = Account('Tan',Decimal('50.00')) #calling Account with attribute 
account1.deposit(Decimal('1000.00')) #calling deposti function 
account1.withdraw(Decimal('-500.00')) #calling withdraw function 

print(account1.name)
print(account1.balance)
print(account1.deposit)