class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def answer(board):
            for row in range(0,len(board)): #row and col loop is mainly for traversing the whole matrix as we use two loops same.
                for col in range(0, len(board[0])):
                    
                    if board[row][col]==".":
                        for char in "123456789":  #here checking all the possible values from 1-9. which can be inserted in place of "."
                            if isvalid(row, col, char, board)==True:
                                board[row][col]=char
                                
                                if answer(board)==True:  #calling for next recursion an if it returs true its the end
                                    return True
                                else:
                                    board[row][col]="."  #if the value is not valid in that place, again place "." into it.
                        return False        
            return True
        
        def isvalid(row, col, char, board):
            #checking for all 9 rows, 9 columns and small 3X3 matrix
            
            for i in range(0,9):
                #checking for all the rows of same column
                if board[i][col] == char:
                    return False
                
                #checking for all the columns of same row
                if board[row][i] == char:
                    return False
                
                #checking for 3X3 sub-boxes of the matrix
                if board[3 * (row//3) + i//3][3*(col//3)+i%3] == char:
                    return False
            return True
        answer(board) # calling the fucntion
        
        
        """
        Do not return anything, modify board in-place instead.
        """
        
