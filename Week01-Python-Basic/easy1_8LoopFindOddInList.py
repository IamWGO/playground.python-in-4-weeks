# E 1.8 Even numbers in lists (Lists, Loops)
# Create a function that takes in a list of integer as arguments,
# and returns how many even numbers there are in the list.


def return_even_numbers(arg) -> []:
    return_numbers = []
    for num in arg:
        if num % 2 != 0:
            return_numbers.append(num)
    return return_numbers


numbers = []
print("\n input 10 numbers.")
for x in range(10):
    new_number = input(f'Your String {x + 1} ? ')
    numbers.append(int(new_number))

print(f"Your numbers {numbers}")

print("\n returnerar hur många jämna tal det finns i listan")
print(f"Even numbers : {return_even_numbers(numbers)}")

