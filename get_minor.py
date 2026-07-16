import numpy as np
def get_minor(A):
    newA=np.array(A) #array instead of nested list
    for i in lst: #list is all combinations
        VertexSubset=[1] # VertexSubset is just one combination
        for j in VertexSubset:
            Index=j-1
            matrix1=np.delete(newA,Index,axis=0)
            matrix2=np.delete(matrix1,Index,axis=1)
            newA=matrix2
    return newA

A = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

B=get_minor(A)
print(B)
