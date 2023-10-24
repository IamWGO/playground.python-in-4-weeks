# M 2.1 Many arguments
# Create a function that accepts any number of numbers as positional arguments
# and prints the sum of those numbers.
# Remember that we can use the sum function to add the values in an iterable.

def get_input_number(text) -> int:
    while True:
        try:
            input_number = int(input(f'{text} '))
            return input_number
        except ValueError:
            print("The input is not a number.")


def add_numbers(*args) -> int:
    product = 1
    for args in args:
        product += args
    return product


def main():
    max_number = get_input_number("input the max number: ")
    numbers = []

    for i in range(max_number):
        input_number = get_input_number(f"input the number {i+1}: ")
        numbers.append(input_number)

    print(f"\nSome of input numbers: {add_numbers(*numbers)}")


if __name__ == '__main__':
    main()
