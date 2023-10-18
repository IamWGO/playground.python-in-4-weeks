# E 1.11 Loop through Dictionaries (Dictionaries, Loops)
# 1. Create a dictionary where the keys are numbers between 1 and 15 and the values are the squares of the keys.
# 2. Print each key-value pair on a new line.
# 3. Calculate and print the sum of all values in the dictionary.


squares_dict = {}
# Populate the dictionary with key-value pairs
for num in range(1, 16):
    squares_dict[num] = num ** 2

# Print each key-value pair on a new line
for key, value in squares_dict.items():
    print(f" {key}: {value}")


# sum_of_values = 0
# for key, value in squares_dict.items():
#     sum_of_values += value

print("Sum of all values:", sum(squares_dict.values()))


# [num for num in nums]
# [[num,num*2] for num in nums]