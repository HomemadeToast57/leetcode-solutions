def ZeroMatrix(matrix):
    # find coordinates of 0s
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 0:
                setNone(matrix, r, c) # set row and column to None
    
    #switch Nones to 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == None:
                matrix[i][j] = 0
    return matrix
                
def setNone(matrix, r, c):
    #set row to 0
    for i in range(len(matrix[r])):
        if matrix[r][i] != 0:
            matrix[r][i] = None
    
    # set column to 0
    for i in range(len(matrix)):
        if matrix[i][c] != 0:
            matrix[i][c] = None
            

print(ZeroMatrix([[1,2,3],[4,0,6],[7,8,9]])) # [[1,0,3],[0,0,0],[7,0,9]]