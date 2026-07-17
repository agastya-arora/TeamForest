import numpy as np
import get_all_vertex_subsets_of_size_i as subset
import copy
def get_minor(A,n,i):#the size of vertex subset we are looking at
    #newA=np.array(A) #array instead of nested list
    
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
#print(get_minor([[1,2,6,3],[8,9,1,4],[1,1,2,2],[1,2,3,4]],4,2))
'''A = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

B=get_minor(A)
print(B)'''