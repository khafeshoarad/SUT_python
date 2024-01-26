def calculate_sum(arr):
    return sum(arr)

def calculate_min(arr):
    return min(arr)

def calculate_max(arr):
    return max(arr)

def calculate_average(arr):
    avg = sum(arr) / len(arr)
    return round(avg, 2)

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def calculate_gcd(arr):
    res = int(arr[0])
    for i in range(1, len(arr)):
        res = gcd(res, int(arr[i]))
    return res

def calculate_lcm(arr):
    lcm = arr[0]
    for i in arr[1:]:
        lcm = lcm * i // gcd(lcm, i)
    return lcm

def main():
    cmds = ["min", "max", "lcd", "sum", "average", "gcd"]
    cmd = input()

    if cmd in cmds:
        arr = []
        while True:
            user_in = input()

            if user_in == 'end':
                break
            arr.append(int(user_in))

        if len(arr) > 0:
            if cmd == "min":
                print(calculate_min(arr))
            elif cmd == "lcd":
                print(calculate_lcm(arr))
            elif cmd == 'max':
                print(calculate_max(arr))
            elif cmd == "average":
                print(calculate_average(arr))
            elif cmd == "gcd":
                print(calculate_gcd(arr))
            elif cmd == 'sum':
                print(calculate_sum(arr))
    else:
        print("Invalid command")

if __name__ == "__main__":
    main()
