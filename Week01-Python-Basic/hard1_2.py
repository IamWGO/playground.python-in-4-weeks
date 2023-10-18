# H 1.2 Roman to Integer
# https://leetcode.com/problems/roman-to-integer/

# Logic form ChatGPT -> refactor roman_dict from array to dictionary
def int_to_roman(num):
    roman_dict = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    roman_numeral = ''
    for key, value in roman_dict.items():
        # check only result > 0 (// floor)
        if num // key > 0:
            # add roman digit
            roman_numeral += value
            # get new num value
            num -= key

    return roman_numeral


# Example usage:
integer_value = 14
print("Roman numeral:", int_to_roman(integer_value))