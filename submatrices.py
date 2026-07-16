#Currently only finds consecutive submatrices
matrix = [
    [3, 5, 1, 3],
    [2, 4, 7, 5],
    [8, 0, 9, 2],
    [2, 1, 5, 0]
]
n=len(matrix)
i=3
for x in range(n - i + 1):
    for t in range(n - i + 1):
        new = [row[t:t+i] for row in matrix[x:x+i]]
        print(new)
