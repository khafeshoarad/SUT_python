import numpy as np

def calculate_determinant(matrix):
    return np.linalg.det(matrix)

def find_max_determinant_matrices(matrices):
    max_determinant = float('-inf')
    max_matrices = None

    for i in range(len(matrices)):
        for j in range(i + 1, len(matrices)):
            product_matrix = np.dot(matrices[i], matrices[j])
            determinant = calculate_determinant(product_matrix)

            if determinant > max_determinant:
                max_determinant = determinant
                max_matrices = (matrices[i], matrices[j])

    return max_matrices  

def input_matrices(n, m):
    matrices = []
    for _ in range(n):
        matrix = [list(map(float, input().split())) for _ in range(m)]
        matrices.append(matrix)
    return matrices

def main():
    n, m = map(int, input("Enter the dimensions (n m): ").split())
    matrices = input_matrices(n, m)
    
    max_determinant_matrices = find_max_determinant_matrices(matrices)
    
    det1 = calculate_determinant(max_determinant_matrices[0])
    det2 = calculate_determinant(max_determinant_matrices[1])

    if det1 > det2:
        result_matrix = np.linalg.inv(np.dot(max_determinant_matrices[0], max_determinant_matrices[1]))
    elif det2 > det1:
        result_matrix = np.linalg.inv(np.dot(max_determinant_matrices[1], max_determinant_matrices[0]))
    else:
        result_matrix = np.linalg.inv(np.dot(max_determinant_matrices[1], max_determinant_matrices[0]))
    
    np.set_printoptions(formatter={'float': '{: 0.3f}'.format})
    
    formatted_matrix = '\n'.join(' '.join(map(str, row)) for row in result_matrix)
    print(formatted_matrix)

if __name__ == "__main__":
    main()
