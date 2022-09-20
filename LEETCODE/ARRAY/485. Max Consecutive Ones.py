class Solution(object):
    def findMaxConsecutiveOnes(self, nums):      
        
#       Optimized solution
#       T.C -> O(N)
#       S.C -> O(1)

        maxi=0
        count=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
                maxi=max(maxi,count)
            else:
                count=0
        return maxi
            
        
        
        
        """
        :type nums: List[int]
        :rtype: int
        """
        
