# M 1.4 List backwards
# Create a function that takes in two lists.
# The function returns true/false if one list is the other backwards.

def is_backwards(arg_list1, arg_list2) -> bool:
    return arg_list1 == arg_list2[::-1]


list1 = ["a", "b", "c"]
list2 = ["c", "b", "a"]
print(f"list 1: {list1}")
print(f"List 2: {list2}")
print(f"if one list is the other backwards: {is_backwards(list1, list2)}")

