def transpose(matrix):
    matrix_transpose = list(map(list, zip(*matrix))) # assign result 
    return matrix_transpose                 
