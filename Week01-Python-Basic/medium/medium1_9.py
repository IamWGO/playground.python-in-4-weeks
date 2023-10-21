# M 1.9 Invert a Dictionary
# Create a dictionary of objects where the keys are unique, but the values are not.
# Write a function to invert the dictionary, by making the values
# from the original dictionary to keys and the keys from the original dictionary
# to the host in the new one.

def invert_dictionary(dictionary) -> {}:
    invert_dict = {}
    for key, value in dictionary.items():
        if value not in invert_dict:
            invert_dict[value] = [key]
        else:
            invert_dict[value].append(key)
    return invert_dict

def main():
    show_time = {'movie1': '11:00am',
                 'movie2': '11:00am',
                 'movie3': '3:00pm',
                 'movie4': '5:00pm'}

    print(f"List by movie: {show_time}")
    print(f"List by time: {invert_dictionary(show_time)}")


if __name__ == '__main__':
    main()
