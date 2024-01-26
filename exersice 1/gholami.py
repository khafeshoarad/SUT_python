def to_binary(n):
    return "{:032b}".format(int(n))

def main():
    rast = to_binary(input("Enter the first number: "))
    chap = to_binary(input("Enter the second number: "))
    dt = chap + rast

    ns = []
    for _ in range(int(input("Enter the number of queries: "))):
        ns.append(int(input("Enter a query number: ")))

    for n in ns:
        result = "yes" if dt[-n-1] == "1" else "no"
        print(result)

if __name__ == "__main__":
    main()
