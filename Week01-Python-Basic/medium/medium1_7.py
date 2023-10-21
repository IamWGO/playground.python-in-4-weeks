# M 1.7 The Robber's Language
# Make a program that translates a string into the robber language.
# ### Code from ChatGPT because I don't understand the logic
def get_input_string(text):
    while True:
        user_input = input(text)
        if not user_input:
            print("The string should contain only '(' and ')'")
            continue
        return user_input


def to_rovarspraket(text):
    vowels = "AEIOUaeiou"
    translated_text = ""

    for char in text:
        if char.isalpha() and char not in vowels:
            translated_text += char + "o" + char
        else:
            translated_text += char

    return translated_text


def main():
    input_text = get_input_string("Input some string : ")
    robber_language_text = to_rovarspraket(input_text)
    print(robber_language_text)


if __name__ == '__main__':
    main()
