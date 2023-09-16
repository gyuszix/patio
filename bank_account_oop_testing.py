class BankAccount:
    def __init__(self, account_number, account_holder, account_balance=0.0):
        self._account_number = account_number
        self._account_holder = account_holder
        self._account_balance = account_balance

    def get_balance(self):
        return self._account_balance

    def deposit(self, deposit_amount):
        if deposit_amount > 0:
            self._account_balance += deposit_amount
            print(f'Deposited amount : {deposit_amount}, New balance: {self._account_balance}')
        else:
            print('Invalid amount')

    def withdraw(self, withdrawal_amount):
        if 0 < withdrawal_amount <= self._account_balance:
            self._account_balance -= withdrawal_amount
            print(f'Withdrawn amount: {withdrawal_amount}, New balance: {self._account_balance}')
        else:
            print(f'Invalid amount')


class Transactions:
    @staticmethod
    def transfer(sender_account, receiver_account, transfer_amount):
        if sender_account.get_balance() >= transfer_amount:
            sender_account.withdraw(transfer_amount)
            receiver_account.deposit(transfer_amount)
            print(f'Transaction complete')
        else:
            print('Insufficient amount')

#
# jules = BankAccount('00323', 'Jules')
# jenny = BankAccount('00324', 'Jenny')
#
# print(jules.get_balance())
# print(jenny.get_balance())
#
#
# jules.deposit(1938.3)
# jenny.deposit(567.3)
#
#
# Transactions.transfer(jules, jenny, 124444)
# Transactions.transfer(jenny, jules, 4567.23)
# Transactions.transfer(jules, jenny, 10000)
#
#
#
# print(jules.get_balance())
# print(jenny.get_balance())
