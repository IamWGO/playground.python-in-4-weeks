# E 1.8 Even numbers in lists (Lists, Loops)
# Create a function that takes in a list of integer as arguments,
# and returns how many even numbers there are in the list.
def get_input_number(text) -> int:
    while True:
        try:
            number = int(input(f'{text} '))
            return number
        except ValueError:
            print("The input is not a number.")


def return_even_numbers(arg) -> []:
    return_numbers = []
    for num in arg:
        if num % 2 != 0:
            return_numbers.append(num)
    return return_numbers


numbers = []
print("\n input 10 numbers.")
for x in range(10):
    new_number = get_input_number(f'Your number {x + 1} ? ')
    numbers.append(new_number)

print(f"Your numbers {numbers}")

print("\n returnerar hur många jämna tal det finns i listan")
print(f"Even numbers : {return_even_numbers(numbers)}")

