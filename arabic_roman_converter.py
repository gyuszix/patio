# this caused me a lot of anguish, but the trick is to make a fucking dictionary
# use the dictionary to subtract from the value until you arrive at zero
# just add it to your string until your get the actual value
# less effective but more intuitive way of doing this is to use while loops and just
# check for each fucking number
# overall spent way too fucking long on this fucking kata


def solution(n):
    roman_numerals = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
        10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
        100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
        1000: 'M'
    }

    result = ""
    for value in sorted(roman_numerals.keys(), reverse=True):
        while n >= value:
            # Print the value being subtracted
            print(f"Subtracting {value}")

            # Append the corresponding Roman numeral to the result
            result += roman_numerals[value]

            # Subtract the value from num
            n -= value

    return result
