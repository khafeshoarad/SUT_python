def build_game_grid(number, cmds):
    row_cnt = cmds.count("B")
    game = [['.' for _ in range(number)] for _ in range(row_cnt + 1)]
    game[0][0] = "*"
    row, col = 0, 0

    for cmd in cmds:
        if cmd == "R":
            col += 1
        elif cmd == "L" and col > 0:
            col -= 1
        elif cmd == "B":
            row += 1

        # Check if the new position is within the grid
        if 0 <= row <= row_cnt and 0 <= col < number:
            # Mark the cell as visited by replacing '*' with '.'
            game[row][col] = '*'

    return game

def print_game_grid(game):
    for row in game:
        for cell in row:
            print(cell + " ", end="", sep="")
        print()

def main():
    number = int(input("Enter the size of the grid: "))

    cmds = []
    while True:
        user_in = input("Enter a command ('END' to finish): ")

        if user_in == 'END':
            break
        cmds.append(user_in)

    game = build_game_grid(number, cmds)
    print_game_grid(game)

    if game[-1][-1] == '.':
        print("There's no way out!")

if __name__ == "__main__":
    main()
