class Solution(object):
    def sortColors(self, nums):
        low,mid,high=0,0,len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                temp = nums[mid]
                nums[mid] = nums[low]
                nums[low] = temp
                mid+=1
                low+=1
            elif nums[mid]==1:
                mid+=1
            elif nums[mid]==2:
                temp=nums[mid]
                nums[mid]=nums[high]
                nums[high] = temp
                high-=1
        return nums
        
        
        
        
        
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
