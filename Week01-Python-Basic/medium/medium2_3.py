# M 2.3 Printing a range
# Using * unpacking and range, print the numbers 1 to 20, separated by commas.
# You will have to provide an argument for print function's sep parameter for this exercise.
#
# Additional: Modify your code from exercise 2.3 so that each number prints on a different line.
# You can only use a single print call.

def unpacking_range_numbers(*args):
    print("Positional arguments:")
    print(args)


def printNumbers(max_numbers):
    [print(num + 1) for num in range(max_numbers)]


def main():
    numbers = [num + 1 for num in range(20)]
    unpacking_range_numbers(*numbers)
    printNumbers(20)


if __name__ == '__main__':
    main()
