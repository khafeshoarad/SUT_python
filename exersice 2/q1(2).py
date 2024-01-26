def find_divisors(number):
    return sum(i for i in range(1, number + 1) if number % i == 0)

def change_mabna(number, base):
    res = ""
    quotient = number
    while quotient > 0:
        remainder = quotient % base
        res = str(remainder) + res
        quotient = quotient // base
    return int(res)

def main():
    n = []
    b = []

    while True:
        x, y = map(int, input("Enter x and y (space-separated, or -1 -1 to exit): ").split())

        if x == -1 and y == -1:
            break

        if 2 <= y <= 9 and 1 <= x <= 1000:
            n.append(x)
            b.append(y)
        else:
            print("Invalid base!")
            exit(0)

    result = sum(change_mabna(find_divisors(n[i]), b[i]) for i in range(len(n)))

    print(result)

if __name__ == "__main__":
    main()
