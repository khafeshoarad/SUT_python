def is_prime_number(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
x, y = map(int, input().split())
prime_count = 0
for num in range(min(x, y), max(x, y) + 1):
    if is_prime_number(num):
        prime_count += 1
if x <= y:
    print(f'main order - amount: {prime_count}')
else:
    print(f'reverse order - amount: {prime_count}')