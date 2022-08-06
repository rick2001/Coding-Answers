class Solution(object):
    def searchMatrix(self, matrix, target):
        # using binary search in 2d matrix
        if len(matrix) == 0: return False
            
        row = len(matrix)
        column = len(matrix[0])
        
        low =0
        high = (row*column)-1
        
        while low<=high:
            mid = (low+high)//2
            if matrix[mid//column][mid%column]==target:
                return True
            elif target < matrix[mid//column][mid%column]:
                high = mid-1
            else:
                low=mid+1
        return False
        
        
        
        
        
        
        
        #using brute force approach
#         for i in range(len(matrix)):
#             for j in range(len(matrix[i])):
#                 if matrix[i][j] == target:
#                     return True
#         else:
#             return False
        
        
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
