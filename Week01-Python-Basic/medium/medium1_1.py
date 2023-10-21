# M 1.1 - Nested lists
# A nested list is a list inside another list.
#
# Write a function like:
#
# 1.Create a nested list where each element is a list containing three numbers.
# 2.Prints the first number from each nested list using a loop.
# 3.Adds a fourth number to each nested list.
# 4.Uses a loop to print the sum of the numbers in each nested list.

def get_input_number(text) -> int:
    while True:
        try:
            number = int(input(f'{text} '))
            return number
        except ValueError:
            print("The input is not a number.")


def main():
    nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print("\n#Prints the first number from each nested list using a loop." +
          "\n#Adds a fourth number to each nested list.\n")
    for i, nested in enumerate(nested_list):
        print(f"first number of {nested} is {nested[0]}")
        input_number = get_input_number(f"{i} - input one more number: ")
        nested_list[i].append(input_number)

    print("\n#Uses a loop to print the sum of the numbers in each nested list.")
    for nested in nested_list:
        print(f"sum of {nested} = {sum(nested)}")


if __name__ == '__main__':
    main()
