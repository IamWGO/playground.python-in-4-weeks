from typing import Optional


def api_function(optional_argument: Optional[str] = None) -> None:
    if optional_argument != None:
        print(f"values : {optional_argument}")
    else:
        print("value is none")


# api_function()
# api_function(["hello", "world", "!"])

def args_operator(a, *args):
    print(a)
    print(args)


def args_operator2(a, *args, **kwargs):  # variable, list, dictionary
    print(a)
    print(args)


# args_operator(1, 2, 3, 4, 5)
# Output
# 1
# (2, 3, 4, 5)


def multiply(*args) -> int:
    product = 1
    for args in args:
        product *= args
    return product


print(multiply(2, 3, 4, 4))
