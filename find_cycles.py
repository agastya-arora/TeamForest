def find_cycle(A, i, j): # A is the adjacency list
    n = len(A)
    visited = [False] * n
    parent = [-1] * n

    # DFS to find path from i to j
    def dfs(u):
        visited[u] = True
        for v in A[u]:
            if not visited[v]:
                parent[v] = u
                if v == j or dfs(v):
                    return True
        return False

    dfs(i)

    # Reconstruct path from j to i
    path_nodes = []
    curr = j
    while curr != -1:
        path_nodes.append(curr)
        curr = parent[curr]
    path_nodes.reverse()

    # Convert node path to edge list
    cycle_edges = [(path_nodes[k], path_nodes[k+1]) for k in range(len(path_nodes)-1)]
    cycle_edges.append((i, j)) 

    return cycle_edges
