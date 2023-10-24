# Complete the function/method so that it takes a PascalCase string and returns the string in snake_case notation. Lowercase characters can be numbers. If the method gets a number as input, it should return a string.
#
# Examples
# "TestController"  -->  "test_controller"
# "MoviesAndBooks"  -->  "movies_and_books"
# "App7Test"        -->  "app7_test"
# 1                 -->  "1"



def to_underscore(string):
    capital_letters_tuple = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W','X', 'Y', 'Z')

    word_list = []
    temp_string = ''
    final_string = '_'

    if type(string) == int:
        return  str(string)

    for char in string:
        if char in capital_letters_tuple:
            if temp_string:
                word_list.append(temp_string)
            temp_string = char
        else:
            temp_string += char

    if temp_string:
        word_list.append(temp_string)

    word_list = [x.lower() for x in word_list]

    return final_string.join(word_list)

print(to_underscore('6'))
print(to_underscore('HowdyHowdyHowdy'))






# this so fucking much effort
