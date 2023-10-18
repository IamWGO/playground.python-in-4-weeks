# M 1.7 Rövarspråket
# Gör ett program som översätter en sträng till rövarspråket.
# (https://sv.wikipedia.org/wiki/R%C3%B6varspr%C3%A5ket)

# M 1.7 The Robber's Language
# Make a program that translates a string into the robber language.
# ### Code from ChatGPT

def to_rovarspraket(text):
    vowels = "AEIOUaeiou"
    translated_text = ""

    for char in text:
        if char.isalpha() and char not in vowels:
            translated_text += char + "o" + char
        else:
            translated_text += char

    return translated_text


# Example usage:
input_text = "Hello"
robber_language_text = to_rovarspraket(input_text)
print(robber_language_text)
