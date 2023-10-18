# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]


count_number = int(input("How many numbers do you want to input? "))
numbers = []
for i in range(count_number):
    input_number = int(input(f"Number index {i}: "))
    numbers.append(input_number)

target_number = int(input(f"input target: "))

result = []
target_dict = {}

for i, arg1 in enumerate(numbers):
    for j in range(0, len(numbers) - i - 1):
        # get answer
        answer = numbers[i] + numbers[j]
        # Save a + b = c in array
        result.append([i, j, answer])

target_index = []
for nested in result:
    # check if answer(c) == target_number
    if target_number == nested[2]:
        target_index.append([nested[0], nested[1]])

print(target_index)

# target_dict[numbers[i] + numbers[j]] = [i, j]