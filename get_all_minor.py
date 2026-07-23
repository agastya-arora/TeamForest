#returns a list of all minors. It contains the all the corresponding minors for all the vertex subsets of size i. 
import numpy as np
def get_all_minors(A,i):#the size of vertex subset we are looking at
    newA=np.array(A) #array instead of nested list
    lst=get_all_vertex_subsets_of_size_i(i)
    all_minors=[]
    for combination in lst: #lst is the list of all combinations
        # A vertex-subset is one combination
        for index in combination:
            matrix1=np.delete(newA,index,axis=0)
            matrix2=np.delete(matrix1,index,axis=1)
            newA=matrix2
        all_minors.append(newA)
    return all_minors

A = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

B=get_all_minors(A)
print(B)



# returns all subsets for i vertices
# based on get_minors.py
import numpy as np
import get_all_vertex_subsets_of_size_i as subset
import copy
def get_minor(A,n,i):#the size of vertex subset we are looking at    
    lst=subset.get_all_vertex_subsets_of_size_i(n,i)
    all_minors=[]
    for i in lst: #lst is the list of all combinations
        VertexSubset=list(i) # VertexSubset is just one combination
        newA = copy.deepcopy(A)
        for index in VertexSubset:
            index-=1
            newA[index] = [0]*n
            for row in newA:
                row[index] = 0 
        all_minors.append(newA)
    return all_minors
