# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result
# should be {'a': 2, 'b': 1}.
#
# What if the string is empty? Then the result should be empty object literal, {}


def count_freq_of_chars_in_string(s):

    my_dict = {}

    for char in s:
        if char == " ":
            continue
        elif char not in my_dict.keys():
            my_dict[char] = 1
        else:
            my_dict[char] += 1

    return my_dict



