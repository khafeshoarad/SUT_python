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

n, m = map(int,input().split())

matrices = []

for number in range(n):
    
    matrix = []
    for i in range(m):
        
        row_values = [float(value) for value in input().split()]
        matrix.append(row_values)
    
    matrices.append(matrix)       

max_determinant_matrices = find_max_determinant_matrices(matrices)

det1 = calculate_determinant(max_determinant_matrices[0])
det2 = calculate_determinant(max_determinant_matrices[1])

res = np.array([])
if det1 > det2:
    res = np.linalg.inv(np.dot(max_determinant_matrices[0], max_determinant_matrices[1]))
elif det2 > det1:
    res = np.linalg.inv(np.dot(max_determinant_matrices[1], max_determinant_matrices[0]))
else:
    res = np.linalg.inv(np.dot(max_determinant_matrices[1], max_determinant_matrices[0]))
    
np.set_printoptions(formatter={'float': '{: 0.3f}'.format})

# Convert the matrix to the desired format
formatted_matrix = '\n'.join(' '.join(map(str, row)) for row in res)
print(formatted_matrix)