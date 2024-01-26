def find_divisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return sum(divisors)

def change_mabna(number, base):
  res = ""
  quotient = number
  while quotient > 0:
      remainder = quotient % base
      res = str(remainder) + res
      quotient = quotient // base
  return int(res)

n = []
b = []
x = 0
y = 0
while(True):
  

    x, y = input().split()

    if int(x) == -1 and int(y) == -1:
        break
    if int(y) >= 2 and int(y) <= 9 and int(x) >= 1 and int(x) <= 1000:
        n.append(int(x))
        b.append(int(y))
    else:
        print("invalid base!")
        exit(0)
result = 0
for i in range(len(n)):
  divs = find_divisors(n[i])
  mabna = change_mabna(divs, b[i])

  result = result + mabna
print(result)
