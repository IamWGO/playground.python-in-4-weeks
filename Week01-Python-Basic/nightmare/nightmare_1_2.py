# N 1.2 Longest valid parenthesis
# Given a string containing just the characters '(' and ')',
# return the length of the longest valid (well-formed) parentheses
# substring.

def get_input_string(text):
    while True:
        user_input = input(text)
        if not user_input:
            print("The string should contain only '(' and ')'")
            continue
        return user_input


def is_correct_format(input_string):
    return all(char in "()" for char in input_string)


def get_longest_parentheses(input_string):

    parentheses_set = []
    open_parentheses = []
    string_set = ""

    for char in input_string:

        if char == "(":
            open_parentheses.append(char)
            string_set += char
        else:
            # remove the last item of open_parentheses list if not empty
            if len(open_parentheses) > 0:
                open_parentheses.pop()
            string_set += char

        # put parentheses set
        # clear string_set and open_parentheses
        if len(open_parentheses) == 0 and len(string_set) > 0:
            parentheses_set.append(string_set)
            string_set = ""
            open_parentheses.clear()

    # after loop check if open parentheses in the list
    # substring and get parentheses set
    if len(open_parentheses) > 0:
        parentheses_set.append(string_set[len(open_parentheses):])

    # find longest parentheses
    longest_parentheses = ""
    for parentheses in parentheses_set:
        if len(longest_parentheses) < len(parentheses):
            longest_parentheses = parentheses

    print(f" longest_parentheses = {longest_parentheses}")


def main():
    input_string = get_input_string("Input the characters only '(' or ')': ")
    if not is_correct_format(input_string):
        print("The string should contain only '(' and ')")
        return

    get_longest_parentheses(input_string)


main()

# Example 1:
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
# Example 2:
#
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
# Example 3:
#
# Input: s = ""
# Output: 0
#
# Constraints:
#
# 0 <= s.length <= 3 * 104
# s[i] is '(', or ')'.


#
# def solution1(input_string_value):
#     open_parentheses = []
#     close_parentheses = []
#     parentheses_set = []
#     string_set = ""
#     index = 0
#     for index, char in enumerate(input_string_value):
#
#         if char == "(":
#             open_parentheses.append(char)
#             string_set += char
#         else:
#             if len(open_parentheses) > 0:
#                 open_parentheses.pop()
#                 string_set += char
#             else:
#                 close_parentheses.append(char)
#                 string_set = ""
#
#             if len(open_parentheses) == 0 and len(string_set) > 0:
#                 parentheses_set.append(string_set)
#
#     print(f" start = {parentheses_set}")
#     max_length_item = max(parentheses_set, key=len)
#     print(max_length_item)
#
#
# def solution2(input_string_value):
#     open_parentheses = []
#     close_parentheses = []
#     parentheses_set = []
#     string_set = ""
#     index = 0
#     while index < len(input_string_value):
#         if input_string_value[index] == "(" and input_string_value[index + 1] == ")":
#             string_set += "()"
#             print(string_set)
#             index += 2
#         else:
#             char = input_string_value[index]
#
#             if char == "(":
#                 open_parentheses.append(char)
#                 string_set += char
#             else:
#                 print(open_parentheses)
#                 if len(open_parentheses) > 0:
#                     open_parentheses.pop()
#                     string_set += char
#                 else:
#                     close_parentheses.append(char)
#                     string_set = ""
#
#             index += 1
#
#             if len(open_parentheses) == 0 and len(string_set) > 0:
#                 parentheses_set.append(string_set)
#
#     print(f" start = {parentheses_set}")
#     # max_length_item = max(parentheses_set, key=len)
#     # print(max_length_item)
#
