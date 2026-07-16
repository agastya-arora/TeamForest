def detect_cycle(A): #A is an adjacency list (dictionary in python)
    NumOfVertices=0
    for i in A:         #loops through all the keys
        NumOfVertices+=1  
    visited= [False]*NumOfVertices #to keep a record of all visited ones during dfs

    def DFS(vertex,parent):
        visited[vertex]=True
        for neighbor in A[vertex]:
            if visited[neighbor]==False:
                if DFS(neighbor,vertex):
                    return True
            else:
                if neighbor!=parent:
                    return True
        return False
    
    for i in range(NumOfVertices):
        if visited[i]==False:
            if DFS(i,parent=-1):
                return True
    return False

A1 = {                              #A1 has a cycle
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 4],
    3: [1, 4],
    4: [2, 3]
}
A2 = {                             #A2 is a tree
    0: [1, 2],
    1: [0, 3],
    2: [0, 4],
    3: [1],
    4: [2]
}

print(detect_cycle(A1))  #True
print(detect_cycle(A2))  #False