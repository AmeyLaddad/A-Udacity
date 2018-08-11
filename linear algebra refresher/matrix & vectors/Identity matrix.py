def identity_matrix(n):
    
    identity = [[0 for row in range(n)] for col in range(n)]
    for i in range (n):
        for j in range (n):
            if i == j:
                identity[i][j] = 1
            else:
                identity[i][j] = 0
        
    return identity
    
print(identity_matrix(5))
