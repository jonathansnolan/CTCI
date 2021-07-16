
def zeromatrix(matrix):
    # First Copy the Matrix
    i = []
    for k in matrix:
        copy = []
        zeros = []
        for u in k:
            copy.append(u)
            zeros.append(0)
        i.append(copy)

    # ROWS

    for k in range(len(matrix)):
        if 0 in matrix[k]:
            i[k] = zeros

    #COLUMNS

    for u in range(len(matrix[0])):
        for k in range(len(matrix)):
            if matrix[k][u] == 0:
                for k in range(len(matrix)):
                    i[k][u] = 0
    return i



print(zeromatrix([[1,2,3,4],
                  [2,4,0,4],
                  [7,0,5,4],
                  [1,1,1,1]]))
