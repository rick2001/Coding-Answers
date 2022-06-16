# finding the transpose of a matrix
class Solution(object):
    def rotate(self, matrix):
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
