
def even_or_not(number):
    return True if number % 2 == 0 else False


def generate_n_numbers(n, low, high):

    import sys, random

    while n > (high - low):
        print("n can't be bigger than the difference between high and low")
        sys.exit()
    arr = []
    while True:
        random_int = random.randint(low, high)
        if random_int not in arr:
            arr.append(random_int)
        if len(arr) == n:
            break
    #arr.sort()
    return arr



