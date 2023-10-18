# E 1.3 - Intervall (If-else)
# Skapa funktionen in_range(lower, upper)
# som avgör ifall ett tal är inom det angivna intervallet.
# Om talet finns i ändpunkterna räknas det som inom intervallet.
#
# if number >= 10 and number <=20:
# if 10 <= number <= 20:

def is_number_in_range(number):
    if 10 <= number <= 20:
        print(f"number {number} is in range.")
    else:
        print(f"number {number} is not in range.")


inputNumber = int(input('Your number? '))

print('your number :', inputNumber)
is_number_in_range(inputNumber)
