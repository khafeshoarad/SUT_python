def generate_pascal_triangle(number):
    triangle = [[0 for _ in range(number)] for _ in range(number)]

    for i in range(number):
        for j in range(i + 1):
            if j == 0 or j == i:
                triangle[i][j] = 1
            else:
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    return triangle

def print_pascal_triangle(triangle):
    for line in range(len(triangle)):
        for i in range(line + 1):
            print(str(triangle[line][i]) + " ", end="")
        print()

def main():
    number = int(input("Enter the number of rows for Pascal's Triangle: "))
    
    pascal_triangle = generate_pascal_triangle(number)
    print_pascal_triangle(pascal_triangle)

if __name__ == "__main__":
    main()
