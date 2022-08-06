class Solution(object):
    def maxSubArray(self, nums):
        sumi=0
        maxi=nums[0]
        for i in range(len(nums)):
            sumi+=nums[i]
            if sumi > maxi:
                maxi =sumi
            if sumi<0:
                sumi=0
        return maxi
            
        """
        :type nums: List[int]
        :rtype: int
        """
        
