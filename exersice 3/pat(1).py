input_string = input("Enter space-separated numbers: ")
numbers = input_string.split(" ")

# Sort the numbers based on their integer values
sorted_numbers = sorted(numbers, key=lambda x: int(x[1:]))

# Print the sorted numbers without their integer values
for item in sorted_numbers:
    print(item[0], end="")
