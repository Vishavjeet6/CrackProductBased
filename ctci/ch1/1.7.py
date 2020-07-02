def rotate_matrx(matrix):
    n = len(matrix[0])
    # square matrix
    if n==0 or n != len(matrix):
        return 0

    for layer in range(n//2):
        start =  layer



matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
print(rotate_matrix(matrix))