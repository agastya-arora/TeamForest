import generate_list as gs
def list_to_matrix(vertices, list):
    '''
    Args: 
      vertices: number of vertices that the graph has.
      string: A list/string representation of the adjacency matrix.

    Outputs:
      G: the adjacency matrix of graph G.
    '''
    # Extract n from the beginning of the string/list
    n = int(list[vertices-1]) 

    # Initialize zero matrix
    G = [[0 for _ in range(vertices)] for _ in range(vertices)] 

    # Start reading edge data from index 1 (since index 0 is n)
    CountListItem = 0 
    
    for x in range(n):
        CountColumn = n
        for z in G[x][n:]:
            G[x][CountColumn] = int(list[CountListItem])
            CountListItem += 1
            CountColumn += 1

    # Mirror the top-right block to the bottom-left to maintain symmetry
    for i in range(n):
        for j in range(vertices):
            G[j][i] = G[i][j]
            
    return G
'''vertices = int(input('Number of Vertices: '))
for x in create_matrix(vertices,gs.generate_list(vertices)):
    print(x)'''



    
