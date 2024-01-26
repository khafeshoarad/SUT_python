def is_prime_number(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes_in_range(start, end):
    prime_count = 0
    for num in range(min(start, end), max(start, end) + 1):
        if is_prime_number(num):
            prime_count += 1
    return prime_count

def main():
    x, y = map(int, input("Enter two numbers separated by space: ").split())

    prime_count = count_primes_in_range(x, y)

    order = "main" if x <= y else "reverse"
    print(f'{order} order - amount: {prime_count}')

if __name__ == "__main__":
    main()
