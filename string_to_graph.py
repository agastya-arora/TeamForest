import generate_string as gs

def create_matrix(vertices):
    string = gs.generate_string(vertices)
    print(string)
    LengthOfString = len(string) -1
    n=int(string[LengthOfString])#Number of rows
    m = int((len(string)-1)/n)#Number of columns
    G = [[0 for _ in range(vertices)] for _ in range(vertices)] #Zero matrix

    CountStringItem = 0
    for x in range(n):
        CountColumn = n
        for z in G[x][n:]:
            G[x][CountColumn]=int(string[CountStringItem])
            CountStringItem+=1
            CountColumn+=1

    for i in range(n):
        for j in range(vertices):
            #print(G[i][j])
            G[j][i]=G[i][j]
    return G

for x in create_matrix(int(input('Number of Vertices: '))):
    print(x)





    
