class Solution(object):
    def maxSubArray(self, nums):
        start=None     #store teh starting index
        end = None     #store the ending index
        
        maxi_sum=0   #it will store the maximum sum
        maxi_subarray=[]   #it will store the maximum sub_array
        for i in range(len(nums)):
            sumi=0
            for j in range(i,len(nums)):
                sumi+=nums[j]
                if sumi > maxi_sum:
                    start =i     #storing the starting and ending index of maximum sub array sum
                    end=j
                    maxi_sum=sumi
        for i in range(start,end+1):   #storing the values
            maxi_subarray.append(nums[i])
        return f"maximum subarray-> {maxi_subarray}, and sum is-> {maxi_sum}"

obj1 = Solution()
print(obj1.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

#Time Complexity-> O(N^2)
#Space Complexity-> O(N)
