# # this code was created to make a roman numeral converter
# # e.g. 1666 = MDCLXVI
#
#
# def solution(n):
#     pass
#
#
# #
# n = 1001
# roman_num = []
#
# print(solution(n))
#
# if n / 1000 > 1:
#     partial = int((n/1000)) * "M"
#     roman_num.append(partial)
#
#
# if n / 500 > 1 and n % 1000 != 0:
#     roman_num.append('D')
#
#
# if n / 100 > 1:
#     partial = (int((n/100)) % 10) * "C"
#     roman_num.append(partial )
#
# if n / 50 > 1:
#     roman_num.append('L')
#
# print(roman_num)
#

def arabic_to_roman(num):
    if not (0 < num < 4000):
        return "Invalid input. Please enter a number between 1 and 3999."

    roman_numerals = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
        10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
        100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
        1000: 'M'
    }

    result = ""
    for value in sorted(roman_numerals.keys(), reverse=True):
        while num >= value:
            # Print the value being subtracted
            print(f"Subtracting {value}")

            # Append the corresponding Roman numeral to the result
            result += roman_numerals[value]

            # Subtract the value from num
            num -= value

    return result


# Example usage:
arabic_num = 1994
roman_numeral = arabic_to_roman(arabic_num)
print(f"{arabic_num} in Roman numerals is: {roman_numeral}")



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
    