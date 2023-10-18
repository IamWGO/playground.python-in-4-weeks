#File example : work together with textfile.txt
import json

print("\n------------------f = open()--------------------\n")
f = open("textfile.txt")
contents = f.read()
print(contents.upper())
f.close()

print("\n------------------with open() as file--------------------\n")
with open("textfile.txt") as file:
    for line in file:
        print(line)

print("\n-----------------with open() as file and find text---------------------\n")

substring = "TURBO!"
found = False
with open("textfile.txt") as file:
    for line in file:
        print(line)
        if substring in line:
            print(f"'{substring}' found in the string.")
            found = True
            break

    if not found:
        print(f"Text {substring} not found")

print("\n-----------------Read json file + exception---------------------\n")

try:
    with open("textfile.json", "r", encoding="utf-8") as file:
        try:
            json_dict = json.load(file)
            print(json_dict)
            print(json_dict["glossary"]["title"])
        except json.JSONDecodeError as e:
            print(f"Wrong JSON format: {e}")
        except ValueError:
            print("File is not json format")
except FileNotFoundError:
    print("file not found!!")





