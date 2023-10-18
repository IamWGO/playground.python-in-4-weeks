# [1, 2, 3, 4, 5]
# print(numbers[0:5])

# [1, 3, 5, 7, 9]
# print(numbers[0:10:2])

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(numbers)

# [num for num in nums]
# [[num,num*2] for num in nums]

#
# #Substring
# my_string = "Hello world!"
#
# print("my_string[0:2] ->He")
# print(my_string[0:2])
#
# print("my_string[2:5] ->llo")
# print(my_string[2:5])
#
# print("my_string[2:10] ->llo worl")
# print(my_string[2:10])
#
# print("my_string[2:10:5] ->lo")
# print(my_string[2:10:5])
#
#
# print(22 // 5)
#
# print(str("hello").__class__)
# print(type(str("hello")))
#
#
# print("it's my laptop!!")
# print('it\'s my laptop!!')
# print('she said "Hello lee!"')
# print("she said \"Hello lee!\"""")
#
#
# # my_key = "year"
# # print(my_key in my_dict)
#
#
# f = open("file.txt")
# contents = f.read()
# print(contents.upper())
# f.close()



with open("textfile.txt") as file:
    for line in file:
        print(line)


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
