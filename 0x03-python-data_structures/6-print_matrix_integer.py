#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in range(len(matrix)):
        for e in range(len(matrix[x])):
            print("{}".format(matrix[x][e]), end=' ')
        print()
