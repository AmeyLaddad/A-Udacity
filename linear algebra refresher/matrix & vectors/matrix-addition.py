def matrix_addition(matrixA, matrixB):
    if len(matrixA) != len(matrixB):
        print("Error! Matrices must have the same number of columns !!!")
        return None
    if len(matrixA[0]) != len(matrixB[0]):
        print("Error! Matrices must have the same number of rows !!!")
        return None
    # initialize matrix to hold the results
    matrixSum = []
  
    
    for i in range(len(matrixA)):
        row_A = matrixA[i]
        row_B = matrixB[i]
        row = [] # empty row for now
        for j in range(len(row_A)):
            matrixA_ij = matrixA[i][j]
            matrixB_ij = matrixB[i][j]
            r_ij = matrixA_ij + matrixB_ij
            row.append(r_ij)
        matrixSum.append(row)
    
    return matrixSum

### Test cases ###

A = [
    [2,5,1], 
    [6,9,7.4], 
    [2,1,1], 
    [8,5,3], 
    [2,1,6], 
    [5,3,1]
]

B = [
    [7, 19, 5.1], 
    [6.5,9.2,7.4], 
    [2.8,1.5,12], 
    [8,5,3], 
    [2,1,6], 
    [2,33,1]
]

matrix_addition(A, B)
