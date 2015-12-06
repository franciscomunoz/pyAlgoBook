#!/usr/bin/python

class CreditCard:
    def __init__(self,customer,bank,acnt,limit,balance = 0):
        self._customer = customer
        self._bank = bank
        self_.accout = acnt self._limit = limit
        self._balance = balance

    def get_customer(self):
        """"Return name of the customer."""
        return self._customer
    
    def get_account(self):
        """Return the card identifying number (typically stored in a string). """
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self):
        """Return current balance."""
        return self._balance

    def charge(self,price):
        """Charge given price to the card, assuming sufficient credit limit

        Return True if charge was processed; False if charge was denied.
        """
        if not isinstance(price,(int,float)):
            raise TypeError('price must be numeric')
        elif price < 0:
            raise ValueError('price cannot be negative')
        if price + self._balance > self._limit: #if charge would exceed limit
            return False                        #cannot accept charge
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        if not isinstance(amount,(int,float)):
            raise TypeError('amount must be numeric')
        elif amount < 0:
            raise ValueError('amount cannot be negative')
        self._balance -= amount
    
