# E 1.2 Jämnt eller udda (If-else)
# Skriv en funktion som tar in en enskild siffra
# och skriver ut om den är udda eller jämn.

def get_input_number(text) -> int:
    while True:
        try:
            number = int(input(f'{text} '))
            return number
        except ValueError:
            print("The input is not a number.")


def odd_or_even(number):
    if number % 2 == 0:
        print("Odd")
    else:
        print("Even")


def main():
    inputNumber = get_input_number('Your number? ')
    print('your number :', inputNumber)
    odd_or_even(inputNumber)


main()