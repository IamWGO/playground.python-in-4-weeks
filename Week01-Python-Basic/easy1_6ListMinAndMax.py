# E 1.6 Smallest and largest (Lists)
# 1.Creates a list of 10 random integers.
# 2.Looking for a built-in function to find the largest number.
# 3.Looking for a function to find the smallest number.
# 4.Finds the sum of all numbers in the list.
# 5.Sorts the list from lowest to highest.

numbers = []
print("1.Skapar en lista med 10 slumpmässiga heltal.")
for x in range(10):
    new_number = input(f'Your String {x + 1} ? ')
    numbers.append(int(new_number))

print("\n2.Letar reda på en inbyggd funktion för att hitta det största talet.")
maximum_value = max(numbers)
print("The maximum value in the list is:", maximum_value)

print("\n3.Letar reda på en funktion för att hitta det minsta talet.")
maximum_value = min(numbers)
print("The minimum value in the list is:", maximum_value)

print("\n4.Hittar summan av alla tal i listan.")
maximum_value = sum(numbers)
print("The minimum value in the list is:", maximum_value)

print("\n5.Sorterar listan från lägst till högst.")
sorted_numbers = sorted(numbers)
print(sorted_numbers)
