# E 1.1 Ålderskontroll (If-else)
# Skriv en funktion som tar in användarens ålder
# och sedan skriver ut om de är minderåriga (under 18 år),
# vuxna (mellan 18 och 65) eller pensionärer (över 65).

age = int(input('How old are you?'))

print('your age is :', age)

# elif 18 <= age <= 65:
# elif age >= 18 and age <= 65:
if age < 18:
    print("minderåriga")
elif 18 <= age <= 65:
    print("mellan 18 och 65")
else:
    print("över 65")
