# M 1.3 Largest number
# Create a function that takes a list of integers as arguments and returns the largest number.
# You must not use max()

def get_max_number(numbers_arg) -> int:
    max_number = 0
    for number in numbers_arg:
        if max_number < number:
            max_number = number
    return max_number


numbers = [11, 22, 22, 23, 23, 23, 24, 24, 23, 24]
print(f"numbers in array: {numbers}")
print(f"Maximum number is: {get_max_number(numbers)}")
