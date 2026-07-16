import numpy as np
def get_minor(A,i):#the size of vertex subset we are looking at
    newA=np.array(A) #array instead of nested list
    lst=get_all_vertex_subsets_of_size_i(i)
    for i in lst: #lst is the list of all combinations
        VertexSubset=i # VertexSubset is just one combination
        for index in VertexSubset:
            matrix1=np.delete(newA,index,axis=0)
            matrix2=np.delete(matrix1,index,axis=1)
            newA=matrix2
    return newA

A = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

B=get_minor(A)
print(B)
