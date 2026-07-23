def matrix_to_list(n,G):
    list_rep = [n]
    count1=1
    for row in G:
        count2=1
        if count1<=n:
            for y in row:
                if count2>n:
                    list_rep.append(y)
                count2+=1
        count1+=1
    return list_rep

G = [[0,0,1,1,1],
     [0,0,0,1,1],
     [1,0,0,0,0],
     [1,1,0,0,0],
     [1,1,0,0,0]]
n=2
#input size of matrix
print(matrix_to_list(n,G))
