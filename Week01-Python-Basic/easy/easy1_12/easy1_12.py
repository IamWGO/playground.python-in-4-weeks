# E 1.12 Reading a File:
# Write a Python script that reads a file and prints its contents to the console.
# Create a text file with several lines of text for testing purposes.
# Additional: Modify the script to read the file line by line and print each one with its line number.


def readFileAndPrintContent(filename):
    print("\n1. Reads a file and prints its contents to the console.")
    with open(filename) as file:
        contents = file.read()
        print(contents)


def writeFileWithString(filename, contents):
    print("\n2. Create a text file with several lines of text for testing purposes.")
    try:
        f = open(filename, "w", encoding="utf-8")
        f.writelines(contents)
        print(f"filename: '{filename}'")
        print(f"content: '{contents}'")
    except FileNotFoundError:
        print("file not found!!")


def readAndPrintByLine(filename, searchString):
    print("\n3. Read the file line by line and print each one with its line number.")
    found = False
    with open("textfile.txt") as file:
        for line in file:
            if searchString in line:
                print(f"'{searchString}' found in the string.")
                found = True
                break

        if not found:
            print(f"Text {searchString} not found")


def main():
    readFileAndPrintContent("textfile.txt")

    contents = """I am passionate about mobile application development and excited to continue growing as a Native App developer.
     I am confident that my strong technical skills, commitment to quality, excellent communication abilities, 
     and eagerness to learn will undoubtedly make me a valuable asset to any team."""
    writeFileWithString("textfile2.txt", contents)

    searchString = "TURBO!"
    readAndPrintByLine("file3", searchString)


if __name__ == '__main__':
    main()
