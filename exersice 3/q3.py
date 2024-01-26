import re
def remove_hash_after_at(input_string):
    while '@' in input_string and '#' in input_string:
        at_index = input_string.index('@')
        hash_index = input_string.find('#', at_index)

        if hash_index > at_index:
            input_string = input_string[:hash_index] + input_string[hash_index+1:]
        else:
            break

    input_string = re.sub(' +', ' ', input_string).strip()
    
    
    return input_string.replace(r'\n', "\n")    

input_string = input()

print("Formatted Text: " + remove_hash_after_at(input_string))
