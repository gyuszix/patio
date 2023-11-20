# this fucking task was absolute bullshit bc in the end the guy wanted to have foobar100 output with foobar099 input
# since that ask is actually horseshit, and doesn't have a lick of logic into it, I elected to ignore that shit

def increment_string(strng):
    if strng == '':
        return '1'

    count = 1
    left_string = ''
    right_string = ''

    if not strng[-count].isnumeric():
        return strng + '1'

    while strng[-count].isnumeric():
        right_string += strng[-count]
        count += 1

    right_string = right_string[::-1]

    while right_string[0] == '0':
        right_string = right_string[1:]
        left_string += '0'
        if len(right_string) == 0:
            break

    if right_string == '' and left_string[-1] == '0':
        right_string = '0'
        left_string = left_string[:-1]

    right_string = str(int(right_string) + 1)

    left_string = strng[:-(count - 1)] + left_string

    strng = left_string + right_string

    return strng


print(increment_string('foobar099'))



