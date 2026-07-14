def matrix_to_list(adj_matrix):
    n = len(adj_matrix)
    
    # init empty list
    adj_list = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            #Append only the neighbor
            if adj_matrix[i][j] != 0:
                adj_list[i].append(j)
                
    return adj_list

