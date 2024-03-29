import datetime


class Employee:

    annual_raise_amount = 1.05  # class variable which is then shared between all instances
    num_of_employee = 0  # class variable

    def __init__(self, first, last, salary):
        self.first = first  # all these are instance variables
        self.last = last
        self.salary = salary
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_employee += 1

    def class_intro(self):  # regular method which then will take the instance as he first argument
        return 'This employee is {} {} with the email address: {} who has a renumeration of {}'.format\
            (self.first, self.last, self.email, self.salary)

    def apply_raise(self):  # regular method
        self.salary = int(self.salary * self.annual_raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):  # this one is called a class method
        cls.annual_raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):  # pass a class method as an alternative constructor
        first, last, salary, = emp_str.split('-')
        return cls(first, last, salary)

    @staticmethod
    def is_workday(day):  # static method is used for when the method is related to the class logically but it doesn't the instance nor the class passed as first argument
        if day.weekday() == 5 or day.weekday == 6:
            return False
        return True


class Developer(Employee):
    def __init__(self, first, last, salary, prog_lang):
        super().__init__(first, last, salary)  # this line is for keeping the code DRY and not passing the same arguments again
        self.prog_lang = prog_lang  # this is the new line of attribute for the developer class which inherits from


emp_str_1 = 'Perry-Cox-100000'
emp_str_2 = 'John-Dorian-80000'
emp_str_3 = 'Eliot-Reed-90000'


johndoe = Employee('Christopher', 'Turk', 50000)
janedoe = Employee('Carla', 'Espinosa', 60000)

new_emp_1 = Employee.from_string(emp_str_1)  # instantiation of the new instances passing the alternative constructor
new_emp_2 = Employee.from_string(emp_str_2)  # instantiation of the new instances passing the alternative constructor
new_emp_3 = Employee.from_string(emp_str_3)  # instantiation of the new instances passing the alternative constructor

developer_employee_1 = Developer('Nerd', 'Dejohn', 15000, 'Python')

my_date = datetime.date(2020, 4, 29)
print(developer_employee_1.class_intro())
print(developer_employee_1.prog_lang)

# print(johndoe.__dict__)  # prints the namespaces for the instance
# print(johndoe.apply_raise())
# print(johndoe.__dict__)
# print(Employee.num_of_employee)

# print(Employee.annual_raise_amount)
# Employee.set_raise_amount(1.5)
# print(johndoe.annual_raise_amount)
# print(janedoe.annual_raise_amount)

# print(Employee.is_workday(my_date))  # called is_workday method that belongs to the Employee class and passed ONLY the my date variable as an argument

# print(Employee.num_of_employee)
# print(help(Developer))

from typing import List


# class BankAccount:
#     def __init__(self, account_number, account_holder, account_balance=0.0):
#         self._account_number = account_number
#         self._account_holder = account_holder
#         self._account_balance = account_balance
#
#     def get_balance(self):
#         return self._account_balance
#
#     def deposit(self, deposit_amount):
#         if deposit_amount > 0:
#             self._account_balance += deposit_amount
#             print(f'Deposited amount : {deposit_amount}, New balance: {self._account_balance}')
#         else:
#             print('Invalid amount')
#
#     def withdraw(self, withdrawal_amount):
#         if 0 < withdrawal_amount <= self._account_balance:
#             self._account_balance -= withdrawal_amount
#             print(f'Withdrawn amount: {withdrawal_amount}, New balance: {self._account_balance}')
#         else:
#             print(f'Invalid amount')
#
#
# class Transactions:
#     @staticmethod
#     def transfer(sender_account, receiver_account, transfer_amount):
#         if sender_account.get_balance() >= transfer_amount:
#             sender_account.withdraw(transfer_amount)
#             receiver_account.deposit(transfer_amount)
#             print(f'Transaction complete')
#         else:
#             print('Insufficient amount')

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


# new code challenge:
# Move the first letter of each word to the end of it, then
# add "ay" to the end of the word. Leave punctuation marks untouched.

# ig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !



