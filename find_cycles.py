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
    n = len(adj_list)
    visited = [False] * n

    def dfs(u, parent):
        visited[u] = True
        for v in adj_list[u]:
            if not visited[v]:
                if dfs(v, u):
                    return True
            elif v != parent:
                return True
        return False

    for i in range(n):
        if not visited[i]:
            if dfs(i, -1):
                return True
                
    return False
