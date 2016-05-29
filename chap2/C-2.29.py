#!/usr/bin/python
import datetime
import pdb

class CreditCard:
    def __init__(self,customer,bank,acnt,limit,balance = 0):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance

    def get_customer(self):
        """"Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank's name."""
        return self._bank

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

class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compoints interest and fees."""

    def __init__(self,customer,bank,acn,limit,apr):
        """Create a new predatory credit card instance.

        The initial balance is zero.

        customer    the name of the customer (e.g., 'John Bowman')
        bank        the name of the bank(e.g., 'California Savings')
        acnt        the account identifier (e.g., '5391 0375 9387 5309')
        limit       credit limit (measured in dollars)
        apr         annual percentage rate (e.g., 0.0825 for 8.25% APR)
        counter     add extra $1 everytime a charge exeeds 10 calls in a month
        ref_month   used for comparing months in charge
        """
        super().__init__(customer,bank,acn,limit)   #call super constructor
        self._apr = apr
        self._counter = 0
        self._ref_month = datetime.date.today().strftime("%B")

    def charge(self,price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed.
        Return False ad asseses $5 fee if chrarge is declined.
        """
        sucess = super().charge(price)      #call inherited method
        if not sucess:
            self._balance += 5              #assess penalty
        current_month = datetime.date.today().strftime("%B")
        if current_month == self._ref_month:
            self._counter+=1
            if self._counter >= 10:
                self._balance+=1
        else:
            self._ref_month = current_month
            self._counter = 0
        self._min_monthly_pay = self._balance * .10  #pay this before the end of month
        return sucess                       #caller expects return value

    def make_payment(self, amount):
        super().make_payment(amount)
        self._min_monthly_pay-= amount      #reduce min payment
        print("=>>>>>>>>>> {0}".format(self._min_monthly_pay))

    def process_month(self):
        """Asses monthly interest on outstanding balance."""
        if self._balance > 0:
            #if positive balance, convert PR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr,1/12)
            self._balance *= monthly_factor
            if self._min_monthly_pay > 0:
                self._balance+= self._balance * .02  #penalties for not paying

if __name__ == '__main__':
    wallet = []
    wallet.append(PredatoryCreditCard('John Bowman','California Savings',
                                '5391 0375 9387 5309',2500,.834))
    wallet.append(PredatoryCreditCard('John Bowman','California Federal',
                                '3485 0399 3395 1954',3500,.57))
    wallet.append(PredatoryCreditCard('John Bowman','California Finance',
                                '5391 0375 9387 5309', 5000,.9))

    for val in range(1,17):
        wallet[0].charge(val)
        wallet[1].charge(100*val)
        wallet[2].charge(3*val)

    for c in range(3):
        print('Customer =', wallet[c].get_customer())
        print('Bank = ', wallet[c].get_bank())
        print('Account =', wallet[c].get_account())
        print('Limit =', wallet[c].get_limit())
        print('Balance =',wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(200)
            print('New balance =', wallet[c].get_balance())
        print()
        wallet[c].process_month()
        print('Balance after processing month =',wallet[c].get_balance())
        print()
