class Solution:
     
    #Function to find if there exists a triplet in the 
    #array A[] which sums up to X.
    
    
    #If triplet is a,b,c. so if we consider the arr[i] as a. so i have to find out b and c only.
    #So res=X-arr[i](a) will be the addition of b+c
    def find3Numbers(self,A, n, X):
        A.sort()
        for i in range(n):
            res= X-A[i]    
            low=i+1
            high=n-1
            
            while low < high:
                if A[low]+A[high] == res:
                    return 1     
                elif A[low]+A[high] > res:   # as the array is sorted so if we decrease the high then only the addition will be going equals to res
                    high-=1
                else:        
                    low+=1
        return 0
    
        # Your Code Here

