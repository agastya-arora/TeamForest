from matrix_to_list import matrix_to_list

def find_cycle(A):
    """
    Checks if there's a cycle in a general undirected graph.
    
    Args:
        A: Adjacency matrix of the graph.
        
    Returns:
        bool: True if a cycle exists, False otherwise.
    """
    adj_list = matrix_to_list(A)
    n = len(adj_list) # num of vertices
    visited = [False] * n   # to mark visited vertex

    def dfs(u, parent):
        visited[u] = True #current vertex marked as visited
        for v in adj_list[u]:
            if not visited[v]: # if adjacent vertex has not been visited
                if dfs(v, u): # if adjacent vertex is visited
                    return True # cycle found 
            elif v != parent: # if adjacent vertex is visited and not parent 
                return True # cycle found 
        return False

    for i in range(n): # iterate over all vertices
        if not visited[i]:
            if dfs(i, -1): # if cycle found
                return True
                
    return False
