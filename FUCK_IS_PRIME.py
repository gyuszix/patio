#this mother fucking code checks if a fucking list has any mother fucking primes or not> FUCK
arr = range(100)

for i in range(len(arr)):
    if arr[i] > 3:
        is_prime = True
        for j in range(2, int(arr[i]/2)+1):
            if (arr[i] % j) == 0:
                is_prime = False
                break
            else:
                continue
        print(arr[i], "is prime" if is_prime else "is not prime")
    elif arr[i] in [2,3]:
        print(arr[i], "is prime")
    else:
        print(arr[i], "is not prime")
