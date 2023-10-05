# Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to
# match str2, otherwise returns false.
#
# Notes:
#
# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered.
# Examples
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False

# I managed to write down the code in a few lines, but it seems that this has a big o of m*n
# which can really blow up. Not good enough so now I am going to have to make it more efficient


def scramble(s1, s2):
    for char in s2:
        if char not in s1:
            return False
        if char in s1:
            s1 = s1.replace(char, "", 1)

    return True


# turns out the easiest way of doing this with better time complexity would be
# using hash-maps which is just dictionaries in Python
# Yay


def scramble_2(s1, s2):
    hm_1 = {}
    hm_2 = {}

    for char in s1:
        hm_1[char] = hm_1.get(char, 0) + 1

    for char in s2:
        hm_2[char] = hm_2.get(char, 0) + 1

    for char, count in hm_2.items():
        if char not in hm_1 or hm_1[char] < count:
            return False

    return True

# now the time complexity of this code is actually O(n + m) instead of O(n * M)
