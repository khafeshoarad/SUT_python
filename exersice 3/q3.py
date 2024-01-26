import re

def remove_hash_after_at(input_string):
    while '@' in input_string and '#' in input_string:
        at_index = input_string.index('@')
        hash_index = input_string.find('#', at_index)

        if hash_index > at_index:
            input_string = input_string[:hash_index] + input_string[hash_index + 1:]
        else:
            break

    input_string = re.sub(' +', ' ', input_string).strip()
    return input_string.replace(r'\n', "\n")

def main():
    input_string = input("Enter the text: ")
    formatted_text = remove_hash_after_at(input_string)
    print("Formatted Text:", formatted_text)

if __name__ == "__main__":
    main()
