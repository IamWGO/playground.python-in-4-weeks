# E 1.9 The sum of two lists (Lists, Loops)
# Create a function that takes two equally long lists as arguments.
# Return a list where each element is the sum of the two lists' respective elements.

numbers1 = []
numbers2 = []
numbers3 = []

print("\nSet 1 : input 5 numbers.")
for x in range(5):
    new_number = input(f'Your String {x + 1} ? ')
    numbers1.append(int(new_number))

print("\nSet 1 : input 5 numbers.")
for x in range(5):
    new_number = input(f'Your String {x + 1} ? ')
    numbers2.append(int(new_number))


for i in range(5):
    numbers3.append(numbers1[i] + numbers2[i])

for i in range(5):
    print(f"{numbers1[i]} + {numbers2[i]} = {numbers3[i]}")
