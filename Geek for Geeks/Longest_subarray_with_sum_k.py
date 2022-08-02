class Solution:
    def lenOfLongSubarr (self, A, N, K) :
        
        
        #A-> is the array
        #N-> is the length
        #K-> is the target
        
        mydict = {}
        sum = 0
        maxLen = 0
     
        
        for i in range(N):
     
            # accumulate the sum
            sum += A[i]
     
           
            if (sum == K):
                maxLen = i + 1
     
            
            elif (sum - K) in mydict:
                maxLen = max(maxLen, i - mydict[sum - K])
     
            
            if sum not in mydict:
                mydict[sum] = i
     
        return maxLen
        
