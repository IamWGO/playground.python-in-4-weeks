# E 1.5 List slicing (Lists)
# Write a function like:
#
# 1.Creates a list containing the numbers 1 to 10.
# 2.Uses list slicing to print the first five numbers.
# 3.Uses list slicing to print the last four numbers.
# 4.Prints every other number in the list, starting with the first one.
# 5.Creates a new list that is a copy of the reversed original list.


print("1.Skapar en lista som innehåller numren 1 till 10.")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(numbers)

print("\n2.Använder list slicing för att skriva ut de första fem numren.")
print(numbers[0:5])

print("\n3.Använder list slicing för att skriva ut de sista fyra numren.")
print(numbers[len(numbers) - 4: len(numbers)])

print("\n4.Skriver ut varannat nummer i listan, börjande med det första.")
for i, n in enumerate(numbers):
    print(f"item {i + 1} -> {n}")

print("\n5.Skapar en ny lista som är en kopia av den omvända original listan.")
copy_numbers = numbers
reversed_numbers = copy_numbers[::-1]
print(reversed_numbers)
