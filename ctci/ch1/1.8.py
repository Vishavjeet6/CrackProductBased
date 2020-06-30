def zero_matrix(matrix):
    pos=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                pos.append((i,j))
    for x in pos:
        matrix[x[0]] = [0]*len(matrix[0])
        for i in range(len(matrix)):
            matrix[i][x[1]] = 0
    return matrix

matrix = [
    [1,2,3,4],
    [5,0,7,0],
    [9,0,11,12]
]

print(zero_matrix(matrix))