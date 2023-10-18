# E 1.7 Combine Lists (Lists)
# Create a function that takes two lists of integers as arguments
# and returns a combined and sorted list of them.

def get_input_number(text) -> int:
    while True:
        try:
            number = int(input(f'{text} '))
            return number
        except ValueError:
            print("The input is not a number.")


def combine_lists(arg1, arg2) -> []:
    combine_numbers = arg1 + arg2
    return combine_numbers


numbers1 = []
numbers2 = []
print("\nSet 1 : input 5 numbers.")
for x in range(5):
    new_number = get_input_number(f'Your String {x + 1} ? ')
    numbers1.append(new_number)

print("\nSet 1 : input 5 numbers.")
for x in range(5):
    new_number = get_input_number(f'Your String {x + 1} ? ')
    numbers2.append(new_number)

print("Skapa en funktion som tar två listor med heltal  " +
      "som argument och returnerar en kombinerad och sorterad lista av dessa.")
print(combine_lists(numbers1, numbers2))
