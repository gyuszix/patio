def isIsogram(string):
    string = string.lower()

    repeating = set()

    for char in string:
        if char in repeating:
            return False

        repeating.add(char)

    return True

print(isIsogram("dermeato"))