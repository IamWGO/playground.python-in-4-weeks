# M 1.5 FizzBuzz
# FizzBuzz is a classic interview problem.
#
# Write a function that prints all numbers from 1 to a given number.
# If the number is divisible by 3, print "Fizz". If the number is divisible by 5, print "Buzz".
# If the number is divisible by 3 and 5, print "FizzBuzz".
def get_input_number(text) -> int:
    while True:
        try:
            number = int(input(f'{text} '))
            return number
        except ValueError:
            print("The input is not a number.")


def main():
    range_numbers = get_input_number("Show number from 1 to .. ")

    for num in range(1, range_numbers + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("FiZZ")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


if __name__ == '__main__':
    main()
