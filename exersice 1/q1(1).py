def get_binary_input():
    return bin(int(input()))[2:]

def calculate_difference_and_pad(binary1, binary2):
    diff = abs(len(binary1) - len(binary2))
    
    for _ in range(diff):
        if len(binary2) < len(binary1):
            binary2 = '0' + binary2
        else:
            binary1 = '0' + binary1
    
    return binary1, binary2

def count_different_bits(binary1, binary2):
    count = 0
    for i in range(len(binary1)):
        if int(binary1[i]) ^ int(binary2[i]) == 1:
            count += 1
    return count

def main():
    y = get_binary_input()
    x = get_binary_input()

    y, x = calculate_difference_and_pad(y, x)

    diff_count = count_different_bits(x, y)

    print(diff_count)

if __name__ == "__main__":
    main()
