import numpy as np

def rotateMatrix(matrix):
    tempMatrix = np.zeros((matrix.shape[1],matrix.shape[0]),dtype=int)
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]):
            tempMatrix[y][matrix.shape[0]-1-x]=matrix[x][y]
    return tempMatrix
matrix = np.array([[1,2,3,10],[4,5,6,11],[7,8,9,12]])
ans = rotateMatrix(matrix)
print(ans)