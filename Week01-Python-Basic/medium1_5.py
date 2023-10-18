# M 1.5 FizzBuzz
# FizzBuzz is a classic interview problem.
#
# Write a function that prints all numbers from 1 to a given number.
# If the number is divisible by 3, print "Fizz". If the number is divisible by 5, print "Buzz".
# If the number is divisible by 3 and 5, print "FizzBuzz".

range_numbers = int(input("Show number from 1 to "))

for number in range(1, range_numbers + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("FiZZ")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

