# H 1.3 Happy numbers
# https://leetcode.com/problems/happy-number/

# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# Example 2:
#
# Input: n = 2
# Output: false

def get_input_number(text) -> int:
    while True:
        try:
            input_number = int(input(f'{text} '))
            return input_number
        except ValueError:
            print("The input is not a number.")


happy_number = get_input_number("input your happy number: ")
happy_row = 0
is_happy_number = False

while len(str(happy_number)) > 1:
    is_happy_number = True
    digit_list = []
    operator_string = ""
    number_string = str(happy_number)
    for digit in range(len(number_string)):
        digit_list.append(int(number_string[digit]) ** 2)
        operator_string += " " + number_string[digit] + "**2 " + "+"

    happy_number = sum(digit_list)
    operator_string = operator_string[:-1] + " ="
    print(f"{operator_string} {happy_number}")
    digit_list.clear()

if is_happy_number:
    print("it is happy number ^^")
else:
    print("it is not happy number!!")
