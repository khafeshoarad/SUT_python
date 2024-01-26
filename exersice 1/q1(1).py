y = int(input())
x = int(input())
y=bin(y)
x=bin(x)
x = x[2:]
y = y[2:]

dif = abs(len(x)-len(y))
for _ in range(dif):
  if len(y) < len(x):
    y = '0'+y
  else:
    x = '0'+x
cnt = 0
for i in range(len(x)):
  if (int(x[i]) ^ int(y[i])) == 1:
    cnt = 1 + cnt

print(cnt)