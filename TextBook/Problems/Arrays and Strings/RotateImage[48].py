def RotateMatrix(matrix):
    for i in range(len(matrix)): # transpose
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(len(matrix)): # reverse
        matrix[i].reverse()
        
    return matrix

print(RotateMatrix([[1,2,3],[4,5,6],[7,8,9]]))