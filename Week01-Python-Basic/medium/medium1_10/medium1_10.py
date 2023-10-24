# M 1.10 Copying a File
# Write a program that copies the contents of one file to another file.
# Additional: Modify the script to only copy lines that contain a specific word.

def get_input_number(text) -> int:
    while True:
        try:
            input_number = int(input(f'{text} '))
            return input_number
        except ValueError:
            print("The input is not a number.")


def get_input_string(text):
    while True:
        user_input = input(text)
        if not user_input:
            print("The string should contain only '(' and ')'")
            continue
        return user_input


def copy_content_to_new_file(filename, copyfile):
    with open(filename) as file:
        contents = file.read()
        try:
            f = open(copyfile, "w", encoding="utf-8")
            f.writelines(contents)
            print(f"Already copied file from '{filename}' to '{copyfile}' ")
        except FileNotFoundError:
            print("file not found!!")


def is_update_line_in_range(filename, line_number) -> bool:
    with open(filename) as file:
        lines = file.readlines()
        line_count = len(lines)
        return line_number <= line_count


def update_line(filename, line_number, content):
    with open(filename, 'r+', encoding='utf-8') as file:
        contents = file.readlines()
        for i, line in enumerate(contents):
            if i == line_number - 1:
                contents[i] = line.replace(line, content + "\n")

        file.seek(0)
        file.writelines(contents)


def main():
    copy_content_to_new_file("content.text", "content_copy.text")

    line_number = get_input_number("Which line do you want to update ? ")
    if is_update_line_in_range("content_copy.text", line_number):
        print(f"Line {line_number} is in range")

        inputString = get_input_string(f"Update content in line {line_number}: ")
        update_line("content_copy.text", line_number, inputString)

        print(f"updated line {line_number}: {inputString}")

    else:
        print(f"Line {line_number} not in range")


if __name__ == '__main__':
    main()
