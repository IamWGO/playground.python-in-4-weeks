# M 1.4 List backwards
# Create a function that takes in two lists.
# The function returns true/false if one list is the other backwards.

def get_input_number(text) -> int:
    while True:
        try:
            input_number = int(input(f'{text} '))
            return input_number
        except ValueError:
            print("The input is not a number.")


def get_input_string(text):
    while True:
        user_input = input(text)
        if not user_input:
            print("The string should contain only '(' and ')'")
            continue
        return user_input


def is_backwards(arg_list1, arg_list2) -> bool:
    return arg_list1 == arg_list2[::-1]


def main():
    list1 = []
    list2 = []

    print(f"\nThe function returns true/false if one list is the other backwards.")
    maxItems = get_input_number("Amount of items: ")

    print(f"\nSet 1")
    for index in range(maxItems):
        list1.append(get_input_number(f"Input some thing {index + 1}: "))

    print(f"\nSet 2")
    for index in range(maxItems):
        list2.append(get_input_number(f"Input some thing {index + 1}: "))

    print(f"\nlist 1: {list1}")
    print(f"List 2: {list2}")
    print(f"if one list is the other backwards: {is_backwards(list1, list2)}")


if __name__ == '__main__':
    main()



