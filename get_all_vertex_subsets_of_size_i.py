from itertools import combinations
def get_all_vertex_subsets_of_size_i(n,i): #n=no. of vertices, i=size of the vertex-subset we are looking at
    subset_list=list(combinations(range(0,n),i))
    return subset_list