# E 1.4 - Favoritfrukter (Listor)
# Skriva en funktion som:
#
# 1.Skapar en lista som innehåller fem element, som är dina favoritfrukter.
# 2.Lägger till en ny frukt i listan.
# 3.Ändrar det tredje elementet till en annan frukt.
# 4.Tar bort det sista elementet i listan.
# 5.Skriver ut varje frukt i listan på en ny rad.

list_string = []


def add_string_to_list(string):
    list_string.append(string)


def update_string_in_list(index, string):
    list_string[index - 1] = string


def delete_last_item_in_list():
    list_string.pop()  # removes the last element (5)


def print_list():
    for i, n in enumerate(list_string):
        print(f"item {i + 1} -> {n}")
    # for item in list_string:
    #     print(item)


print("\n1.Skapar en lista som innehåller fem element, som är dina favoritfrukter.")
print("\n2.Lägger till en ny frukt i listan.")
for x in range(5):
    new_string = input(f'Your String {x + 1} ? ')
    add_string_to_list(new_string)

print_list()

print("\n3.Ändrar det tredje elementet till en annan frukt.")
update_string = input(f'Your String to update in index-3 ? ')
update_string_in_list(3, update_string)

print_list()

print("\n4.Tar bort det sista elementet i listan.")
delete_last_item_in_list()

print_list()
