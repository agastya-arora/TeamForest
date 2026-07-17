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
