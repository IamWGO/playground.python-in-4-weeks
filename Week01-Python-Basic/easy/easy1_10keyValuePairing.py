# E 1.10 Basic key-value pairing
# Create a dictionary that represents a person;
# it must contain first name, last name, age and email address.
# Print each piece of information individually using the keys.
# Add a new key-value pair representing the person's hometown.
# Check if the person has a key "middlename". If not, add it with a value of your choice.
# Update the person's age by incrementing it by one.

def print_values(arg_person):
    for key, value in arg_person.items():
        print(f" {key}: {value}")


# print("Skapa en dictionary som representerar en person " +
#       "den ska innehålla förnamn, efternamn, ålder och e-postadress.")

person = {"First Name": "Waleerat",
          "Lastname": "Gottlieb",
          "Age": 44,
          "Email": "waleerat.gottlieb@gmail.com"}

# print("\n Skriv ut varje informationsdel individuellt med hjälp av nycklarna.")
print_values(person)

# print("\nLägg till ett nytt nyckel-värde-par som representerar personens hemstad.")
input_string = input(f'\nYour home town ? ')
person["howe town"] = input_string

print_values(person)

# print("\nKontrollera om personen har en nyckel \"mellannamn\". " +
#       " Om inte, lägg till det med ett värde efter eget val.")

answer = input(f'\nDo you have middle name ?(y/any) ')
if answer.lower() == "y":

    while True:
        input_string = input(f'\nmiddle name ? ')
        if input_string != "":
            person["middle name"] = input_string
            break
        else:
            print("middle name should not be empty")
            answer = input(f'\n Do you still want to add middle name? (y/any) ')
            if answer.lower() != "y":
                break

    print_values(person)
else:
    print("Do not thing")

print("\nUppdatera personens ålder genom att öka den med ett")
person["Age"] += 1

print_values(person)
