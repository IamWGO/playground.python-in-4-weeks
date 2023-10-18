# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

def get_input_number(text) -> int:
    while True:
        try:
            input_number = int(input(f'{text} '))
            return input_number
        except ValueError:
            print("The input is not a number.")


count_number = get_input_number("How many numbers do you want to input? ")
numbers = []
for i in range(count_number):
    input_number = get_input_number(f"Number index {i}: ")
    numbers.append(input_number)

target_number = get_input_number(f"input target: ")

result = []
target_dict = {}

for i, arg1 in enumerate(numbers):
    for j in range(0, len(numbers) - i - 1):
        # get answer
        answer = [i, j, numbers[i] + numbers[j]]
        reversed_answer = [j, i, numbers[i] + numbers[j]]
        # Save a + b = c in array  [1,9,10] == [9,1,10]
        if reversed_answer not in result:
            result.append(answer)

target_index = []
for nested in result:
    # check if answer(c) == target_number
    if target_number == nested[2]:
        target_list = [nested[0], nested[1]]
        target_index.append(target_list)

print(target_index)

# target_dict[numbers[i] + numbers[j]] = [i, j]
