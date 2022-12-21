from decimal import Decimal

class Account:

    def __init__(self, name, balance):
        """Initialize an Account object"""

        #if balance is less than 0.00, raise an exception
        if balance < Decimal ('0.00'):
            raise ValueError('Initial balance must be >= to 0.00.')

        self.name = name 
        self.balance = balance

    def deposit (self,amount):
        """Deposit money to the account"""

        # if amount is less than 0.00, raise an exception 
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')

        self.balance += amount 

    def withdraw (self,amount1):
        """Deposit money to the account"""

        # if amount is more than 0.00, raise an exception 
        if amount1 > Decimal('0.00'):
            raise ValueError('amount must be negative.')

        self.balance += amount1
