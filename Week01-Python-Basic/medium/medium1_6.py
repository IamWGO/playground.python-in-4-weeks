# M 1.6 Every other letter
# Write a function that takes a string as an argument and returns every other letter.

def get_every_other_letter(string) -> str:
    result = ""
    for i in range(len(string)):
        if i % 2 != 0:
            result += string[i]
    return result


def main():
    input_string = input("Input a string: ")
    print(f"Result of every other letter: {get_every_other_letter(input_string)}")


if __name__ == '__main__':
    main()
