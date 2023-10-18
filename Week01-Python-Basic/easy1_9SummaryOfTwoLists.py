# E 1.9 The sum of two lists (Lists, Loops)
# Create a function that takes two equally long lists as arguments.
# Return a list where each element is the sum of the two lists' respective elements.
def get_input_number(text) -> int:
    while True:
        try:
            number = int(input(f'{text} '))
            return number
        except ValueError:
            print("The input is not a number.")

numbers1 = []
numbers2 = []
numbers3 = []

print("\nSet 1 : input 5 numbers.")
for x in range(5):
    new_number = get_input_number(f'Your number {x + 1} ? ')
    numbers1.append(new_number)

print("\nSet 1 : input 5 numbers.")
for x in range(5):
    new_number = get_input_number(f'Your number {x + 1} ? ')
    numbers2.append(new_number)


for i in range(5):
    numbers3.append(numbers1[i] + numbers2[i])

for i in range(5):
    print(f"{numbers1[i]} + {numbers2[i]} = {numbers3[i]}")
