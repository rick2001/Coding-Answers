class Solution(object):
    def majorityElement(self, nums):
        # Using Moores voting algorithm
        count =0
        element=0
        
        for val in nums:
            if count==0:
                element = val
            if element == val:
                count+=1
            else:
                count-=1
        return 
