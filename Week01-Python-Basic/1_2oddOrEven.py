# E 1.2 Jämnt eller udda (If-else)
# Skriv en funktion som tar in en enskild siffra
# och skriver ut om den är udda eller jämn.

def odd_or_even(number):
    if number % 2 == 0:
        print("Odd")
    else:
        print("Even")


inputNumber = int(input('Your number? '))

print('your number :', inputNumber)
odd_or_even(inputNumber)
