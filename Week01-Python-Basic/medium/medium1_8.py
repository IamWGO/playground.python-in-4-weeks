# M 1.8 Counting with Dictionaries
# Given a long string of words, create a dictionary that lists the number of each word in the string.
#

word_counts = {}
input_string = input("Input a sentence: ")
# Split the string into words
words = input_string.split(" ")

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

for key, value in word_counts.items():
    print(f"word: {key} -> {value}")
