number = int(input())

cmds = []

while(True):
  user_in = input()

  if user_in == 'END':
    break
  cmds.append(user_in)

row_cnt = cmds.count("B")
game = [['.' for _ in range(number)] for _ in range(row_cnt + 1)]

game[0][0] = "*"

row = 0
col = 0

for cmd in cmds:

  if cmd == "R":
    col = col + 1
  
  elif cmd == "L" and col > 0:
    col -= 1

  elif cmd == "B":
    row += 1

  # print(row, col)

  # Check if the new position is within the grid
  if 0 <= row <= row_cnt and 0 <= col < number:
      # Mark the cell as visited by replacing '*' with '.'
      game[row][col] = '*'



for i in range(row_cnt + 1):
    for j in range(number):
       
      print(game[i][j] + " ", end="",sep="")
    print()

if game[row_cnt][-1] == '.':
   print("There's no way out!")