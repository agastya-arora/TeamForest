import generate_string as gs

def create_matrix(vertices,string):
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

<<<<<<< HEAD
count2 = 1
for x in range(n):
    count1 = n
    for z in G[x][n:]:
        G[x][count1]=my_string[count2]
        count2+=1
        count1+=1

for i in range(n):
    for j in range(n+m):
        G[j][i]=G[i][j]
for x in G:
    print(x)

'''count3 = 1
for x in range(t):
    count1=m
    for z in G[n:]:
        G[count1][x]=my_string[count3]
        count3+=1
        count1+=1'''
=======
    for i in range(n):
        for j in range(vertices):
            #print(G[i][j])
            G[j][i]=G[i][j]
    return G

vertices = int(input('Number of Vertices: '))
for x in create_matrix(vertices,gs.generate_string(vertices)):
    print(x)

>>>>>>> aca03b1ea7a9267a9151c78083fed2816c5bbe1f



    
