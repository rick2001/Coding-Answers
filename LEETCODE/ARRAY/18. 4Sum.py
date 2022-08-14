# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]




class Solution(object):
    def fourSum(self, nums, target):
        
        
        
        # T.C-> O(N^3)
        # S.C-> O(N)
        
        #same as 3 sum problem...here just we are using 3 loops(4sum) insted of 2loops(3sum)
        #most optimized solution
        array=[]
        nums.sort()
        for i in range(len(nums)-3):
            if i==0 or (i>0 and nums[i]!=nums[i-1]):
                for j in range(i+1, len(nums)-2):
                    if j==i+1 or (j>i+1 and nums[j]!=nums[j-1]):
                        newtarget = target-(nums[i]+nums[j])
                        low=j+1
                        high=len(nums)-1
                        
                        while low < high:
                            if nums[low]+nums[high] == newtarget:
                                array.append([nums[i],nums[j],nums[low],nums[high]])
                                
                                while (low < high and nums[low]==nums[low+1]):
                                    low+=1
                                while (low < high and nums[high]==nums[high-1]):
                                    high-=1
                                low+=1
                                high-=1
                            elif nums[low]+nums[high] < newtarget:
                                low+=1
                            else:
                                high-=1
        return array
                            
        
        
        
        
        
        
        
        
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
