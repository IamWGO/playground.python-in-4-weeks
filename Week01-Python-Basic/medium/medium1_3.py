# M 1.3 Largest number
# Create a function that takes a list of integers as arguments and returns the largest number.
# You must not use max()

def get_input_number(text) -> int:
    while True:
        try:
            input_number = int(input(f'{text} '))
            return input_number
        except ValueError:
            print("The input is not a number.")


def get_max_number(numbers_arg) -> int:
    max_number = 0
    for number in numbers_arg:
        if max_number < number:
            max_number = number
    return max_number


def main():
    numbers1 = []

    maxSet1 = get_input_number("Amount of number list: ")
    for index in range(maxSet1):
        numbers1.append(get_input_number(f"Input a number {index + 1}: "))

    print(f"numbers in array: {numbers1}")
    print(f"Maximum number is: {get_max_number(numbers1)}")



if __name__ == '__main__':
    main()
