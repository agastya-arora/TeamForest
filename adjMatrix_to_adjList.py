import numpy as np
def adjMatrix_to_adjList(matrix):
    #M=matrix.tolist()
    A={}
    m=len(matrix)
    for i in range(m):
        A[i]=[]
        count=-1
        for j in matrix[i]:
            count+=1
            if j==1:
                A[i]+=[count]
    return A

A = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 1, 1, 0]
]

print(adjMatrix_to_adjList(A))



                
