#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    out = len(matrix)
    inner = len(matrix[0])
    for i in range(out):
        for j in range(inner):
            if j == inner - 1:
                print("{:d}".format(matrix[i][j]))
            else:
                print("{:d}".format(matrix[i][j]), end=" ")
    if out == 1 and inner == 0:
        print("")
