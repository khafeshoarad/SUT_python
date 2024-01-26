def calculate_gcd(a, b):
    while b != 0:
        carryover = a & b
        a, b = a ^ b, carryover << 1
    return a

def main():
    z = int(input("Enter the first number: "))
    gholam = int(input("Enter the second number: "))
    ghodrat = int(input("Enter the third number: "))

    gcd_result = calculate_gcd(z, gholam)

    print("GCD:", gcd_result)

    if gcd_result == ghodrat:
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    main()
