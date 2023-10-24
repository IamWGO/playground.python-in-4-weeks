# M 2.2 Many more arguments
# Create a function that accepts any number of positional and keyword arguments,
# and that prints them back to the user.
# Your output should indicate which values were provided as positional arguments,
# and which were provided as keyword argument

def multiply(*args, **kwargs):
    print("Positional arguments:")
    print(args)

    print("Keyword arguments:")
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(f"{key}: {value}")


def main():
    print("M 2.2 Many more arguments ")
    list = [1, 2, 3, 4]
    dict = {"a": "first_value", "b": "second_value"}
    multiply(*list, **dict)


if __name__ == '__main__':
    main()
