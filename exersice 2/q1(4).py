number = int(input())
triangle = [[0 for _ in range(number)] for _ in range(number)]

for i in range(number):
  for j in range(i + 1):

    if j == 0 or j == i:
      triangle[i][j] = 1
    else:
      triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

for line in range(number):
        for i in range(line + 1):
            print(str(triangle[line][i]) + " ", end="")
        print()
