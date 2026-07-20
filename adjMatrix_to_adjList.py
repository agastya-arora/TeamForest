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

def matrix_to_list(adj_matrix):
    n = len(adj_matrix)
    
    # init empty list
    adj_list = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            #Append only the neighbor
            if adj_matrix[i][j] != 0:
                adj_list[i].append(j)
                
    return adj_list

A = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 1, 1, 0]
]

print(adjMatrix_to_adjList(A))



                
