import random

def create_random_graph():
    my_string = [random.randint(1, 5)]
    for x in range(my_string[0]*(random.randint(1,5))):
        my_string.append(random.randint(0,1))
    return my_string

my_string = create_random_graph() #Is a list not a string
print(my_string)
n=my_string[0]
m = int((len(my_string)-1)/n)
#Will give an n,m bipartite graph
vertices = n+m
print(vertices)
G = [[0 for _ in range(vertices)] for _ in range(vertices)] #Adjacency matrix

count2 = 1
for x in range(n):
    count1 = n
    for z in G[x][n:]:
        G[x][count1]=my_string[count2]
        count2+=1
        count1+=1

for i in range(n):
    for j in range(vertices):
        print(G[i][j])
        G[j][i]=G[i][j]

for x in G:
    print(x)




    
