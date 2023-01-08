#User function Template for python3

class Solution:
    def findPath(self, m, n):
        # Optimized solution-2. Lesser noof codes 
        def answer(i, j, given_arr, n, final_arr, ans_string, visited_arr, di_arr, dj_arr):
            if i==n-1 and j==n-1:
                final_arr.append(ans_string)
                return
            
            string = "DLRU"
            for index in  range(0, 4): #loop will be checked 4 times for every recursion as we have 4 direction to check
                nextI=i+di_arr[index]
                nextJ=j+dj_arr[index]
                
                if nextI>=0 and nextJ>=0 and nextI<n and nextJ < n and visited_arr[nextI][nextJ]!=1 and given_arr[nextI][nextJ]==1:
                    visited_arr[i][j]=1
                    answer(nextI, nextJ, given_arr, n, final_arr, ans_string + string[index], visited_arr, di_arr, dj_arr)
                    visited_arr[i][j]=0
        
        
        
        
        i=0
        j=0
        final_arr=[]
        visited_arr= [[0 for col in range(n)] for row in range(n)]
        
        di_arr=[1, 0, 0, -1]
        dj_arr=[0, -1, 1, 0]
        
        if m[0][0]==1:
            answer(i, j, m, n, final_arr, "", visited_arr, di_arr, dj_arr)
        return final_arr
        
        
        
        
        
        
        
    # Optimized solution -1 (Here for every direction we are writing the code seperately. like we will check for 4 direction.
    # so for 4 direction we are writing the code individually. if it was 8 direction so we would have to write the code 8 time for 
    # 8 direction)
    # m is the given array and n is the N*N Matriz size
        # def answer(i, j, given_arr, n, final_arr, ans_string, visited_arr):
        #     if i==n-1 and j==n-1:
        #         final_arr.append(ans_string)
        #         return
            
        #     # Check for downward
        #     if (i+1<n and visited_arr[i+1][j]!=1 and given_arr[i+1][j]==1):
        #         visited_arr[i][j]=1
        #         answer(i+1, j, given_arr, n, final_arr, ans_string+"D", visited_arr)
        #         visited_arr[i][j]=0
                
        #     # Check for left
        #     if (j-1>=0 and visited_arr[i][j-1]!=1 and given_arr[i][j-1]==1):
        #         visited_arr[i][j]=1
        #         answer(i, j-1, given_arr, n, final_arr, ans_string+"L", visited_arr)
        #         visited_arr[i][j]=0
                
        #     # Check for right   
        #     if (j+1<n and visited_arr[i][j+1]!=1 and given_arr[i][j+1]==1):
        #         visited_arr[i][j]=1
        #         answer(i, j+1, given_arr, n, final_arr, ans_string+"R", visited_arr)
        #         visited_arr[i][j]=0
                
        #     # Check for upward
        #     if (i-1>=0 and visited_arr[i-1][j]!=1 and given_arr[i-1][j]==1):
        #         visited_arr[i][j]=1
        #         answer(i-1, j, given_arr, n, final_arr, ans_string+"U", visited_arr)
        #         visited_arr[i][j]=0
        
        # i=0
        # j=0
        # final_arr=[]
        # visited_arr= [[0 for col in range(n)] for row in range(n)]
        # # print(visited_arr)
        # if m[0][0]==1:
        #     answer(i, j, m, n, final_arr, "", visited_arr)
        # return final_arr
