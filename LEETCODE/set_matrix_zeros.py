class Solution(object):
    def setZeroes(self, matrix):
        row = len(matrix)
        column = len(matrix[0])
        column0 = True
        #updating the row and columns which will be zeroes
        for i in range(row):
            if matrix[i][0]==0:
                column0=False
            for j in range(1,column):
                if matrix[i][j] == 0:
                    matrix[i][0] =  0
                    matrix[0][j] = 0
                    
        #making the indexes as 0 which has 0 either in row or in column            
        for i in range(row-1,-1,-1):
            for j in range(column-1,0,-1):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j] = 0
            if column0 == False:
                matrix[i][0]=0
                
                      
                
        return matrix
