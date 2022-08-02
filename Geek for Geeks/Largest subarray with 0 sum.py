#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        # sum =0
        # maxi = 0
        # hashMap={}
        # for i in range(n):
        #     sum+=arr[i]
        #     if sum ==0:
        #         maxi = i+1
        #     else:
        #         if sum in hashMap:
        #             index= i-hashMap[sum]
        #             maxi = max(maxi,index)
                    
        #         else:
        #             hashMap[sum]=i
        # return maxi
        
        
        #or
        sum =0
        maxi = 0
        hashMap={}
        for i in range(n):
            sum+=arr[i]
            if sum ==0:
                maxi = i+1
            elif sum in hashMap:
                index= i-hashMap[sum]
                maxi = max(maxi,index)
                    
            if sum not in hashMap:
                hashMap[sum]=i
        return maxi
                
        
        
