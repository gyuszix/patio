import random, math


def even_or_not(number):
    return True if number % 2 == 0 else False


def generate_n_numbers(n, low, high):

    arr = []
    while True:
        random_int = random.randint(low, high)
        if random_int not in arr:
            arr.append(random_int)
        if len(arr) == n:
            break
    return arr


