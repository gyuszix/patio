def odd_or_even():
    user_input = input('please input your number\n')
    if user_input.isdigit():
        if int(user_input) % 2 == 0:
            return user_input + ' is even'
        elif int(user_input) % 2 != 0:
            return user_input + ' is odd'


print(odd_or_even())
