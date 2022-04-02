# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.


def calculate_tax(price, tax):
    return price * tax


def print_billing_doc():
    tax_rate = 0.1
    products = [{'name': 'Book', 'price': 30},
                {'name': 'Pen', 'price': 5}]

    print(f'Name\tPrice\tTax')

    for product in products:
        tax = calculate_tax(product['price'], tax_rate)
        print(f"{product['name']}\t{product['price']}\t{tax}")


print(__name__)

name = ''
while name != 'your name':
    print('pleae type your name')
    name = input()
print('thanks')

while True:
    print('one')
    player_input_one = input('what comes after one? \n')
    if player_input_one != 'two':
        continue
    player_input_two = input('type 2 \n')
    if player_input_one == 'two':
        if player_input_two == '2':
            break
print('three')


while True:
    print('Who are you?')
    name = input()
    if name != 'joe':
        continue
    print(f'hiya {name} What is the password?')
    password = input()
    if password == 'swordfish':
        break
print('Acces granted')

def hello(name):
    print('howdy\nhello\nbonjour\n ')
    print(name)


