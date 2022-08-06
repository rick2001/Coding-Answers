class Solution(object):
    def spiralOrder(self, matrix):
        
        # we will print the matrix in this order (right direction, down direction, left direction, up direction)
        # top and bottom is the row
        # left and right is the column
        
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])
        demoArray = []
        while (left < right and top < bottom):
            # adding every i in the top row
            for i in range(left,right):
                demoArray.append(matrix[top][i])
            top+=1
            
            # adding every i in the right column
            for i in range(top,bottom):
                demoArray.append(matrix[i][right-1])
            right-=1
                
            if not (left < right and top < bottom):
                break
            
            #adding every i of the bottom row
            for i in range(right-1,left-1,-1):
                demoArray.append(matrix[bottom-1][i])
            bottom-=1
            
            #adding every i in the left column
            for i in range(bottom-1,top-1,-1):
                demoArray.append(matrix[i][left])
            left+=1
            
        # returning the array   
        return demoArray
