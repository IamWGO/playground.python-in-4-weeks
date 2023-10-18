# M 1.2 Most frequent number
# Create a function that takes list as argument,
# and returns the value that occurs the most times in the list.
#

def most_common_number(numbers_arg) -> int:
    common_numbers = {}

    for number in numbers_arg:
        common_number = common_numbers.get(number)
        if common_number is None:
            common_numbers[number] = 1
        else:
            common_numbers[number] += 1

    return max(common_numbers, key=common_numbers.get)


numbers = [11, 22, 22, 23, 23, 23, 24, 24, 23, 24]
print(f"numbers in array: {numbers}")
print(f"Common number is: {most_common_number(numbers)}")
