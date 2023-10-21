# Logic form ChatGPT -> Add print log and I understand concept

def longest_unique_substring(sentence):
    start = 0
    end = 0
    max_length = 0
    max_start = 0
    max_end = 0
    unique_chars = []

    while end < len(sentence):
        print(f"----> loop {end} {sentence}  find {sentence[end]}")

        if sentence[end] not in unique_chars:
            unique_chars.append(sentence[end])
            end += 1
            current_length = end - start
            if current_length > max_length:
                max_length = current_length
                max_start = start
                max_end = end
                print(f"""
                current_length {current_length} = end {end} - start {start}
                if current_length {current_length} > max_length {max_length}:
                max_length {max_length} = current_length {current_length}
                max_start {max_start} = start {start}
                max_end {max_end} = end {end}""")
        else:
            unique_chars.remove(sentence[start])
            start += 1
            print("    remove first char and start+1")

        print(f"""
        |end={end} |start={start} |max_length={max_length} |max_start={max_start} |max_end={max_end} 
        |unique_chars={unique_chars}""")

    print(f"max_start={max_start} max_end={max_end}")
    return sentence[max_start:max_end]


def main():
    # Example usage: pwwkew abcabcbb
    input_string = "pwwkew"
    result = longest_unique_substring(input_string)
    print("Longest unique substring:", result)


if __name__ == '__main__':
    main()

