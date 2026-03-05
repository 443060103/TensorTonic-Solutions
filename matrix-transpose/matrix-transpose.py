import numpy as np

def matrix_transpose(A):
    A = np.array(A)
    N,M = A.shape
    result = np.zeros((M, N))   # create new matrix with swapped shape
    
    for i in range(N):
        for j in range(M):
            result[j][i] = A[i][j]   # swap indices
    
    return result

    A= [[1,2,3],[4,5,6]]
    print(matrix_transpose(A))
