class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        array=[]
        
        for i in range(len(nums)-2):
            
            if i==0 or (i>0 and nums[i]!=nums[i-1]):
                low=i+1
                high=len(nums)-1
                sumi = 0-nums[i]
                
                while low < high :
                    if nums[low]+nums[high]==sumi:
                        array.append([nums[i],nums[low],nums[high]])
                        
                        while (low < high and nums[low]==nums[low+1]):
                            low+=1
                        while (low < high and nums[high]==nums[high-1]):
                            high-=1
                        low+=1
                        high-=1
                    elif nums[low]+nums[high] < sumi:
                        low+=1
                    else:
                        high-=1
        return array
                        
