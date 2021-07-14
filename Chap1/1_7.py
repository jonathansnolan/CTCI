"""
Rotate Matrix

We're going to rotate the exterior rows of a matrix 90 degrees to the right

"""

test = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]


def rotate(matrix):
    ans = []
    for i in range(len(matrix)):
        temp = []
        for j in range(len(matrix[0])):
            temp.append(0)
        ans.append(temp)

    #################
    # step 2: put all the left row on top
    #################

    left = []
    for k in list(range(0,len(matrix))):
        left.append(matrix[k][0])
    left = left[::-1]
    for k in list(range(len(ans[0]))):
        ans[0][k] = left[k]

    ##################
    # step 3: put all the top row on the right
    ##################
    top = matrix[0]
    for k in list(range(0,len(matrix))):
        ans[k][-1] = top[k]

    ##################
    # step 4: put all right side on the bottom
    right = []
    for k in list(range(0,len(matrix))):
        right.append(matrix[k][-1])
    right = right[::-1]
    for k in list(range(len(ans[0]))):
        ans[-1][k] = right[k]
    return ans
    ##################
    # step 5: bottom
print(test)
print(rotate(test))
