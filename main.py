def valid_parentheses(string):
    #this function is supposed to see if the parantheses all have correct ends and beginnengs
    arr = []
    for char in string:
        if char == '(' or char == ')':
            arr.append(char)

    if len(arr) % 2 == 0 and len(arr) != 0:
        arr_1 = arr[0:int((len(arr)/2))]
        arr_2 = arr[int((len(arr))/2):int(len(arr))]
        arr_2.reverse()

        for i in range(len(arr_1)):
            if arr_1[i] == arr_2[i]:
                print('f')
                return False
            if arr_1[i] == ')':
                print('f')
                return False
        print('t')
        return True
    print('f')
    return False


# needs refining
# https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python
# a good idea would be to make two lists and count one by one how many are missing
# also on top of that idea on top just make sure to have a flag like 'begins with ( == yes


from random_functions import generate_n_numbers


print(generate_n_numbers(335,1,336))