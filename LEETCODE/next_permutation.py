class Solution(object):
    def nextPermutation(self, nums):
        if len(nums) == 1:
            return nums

        first_index = None
        second_index = None

        # finding the breaking index (from the last)
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                first_index = i
                break
        # edge case if the input is in this order 5 4 3 2 1. we cant find the the 1st breaking index

        if first_index == None:
            nums.reverse()
            return nums
          
        else:
            for j in range((len(nums) - 1), -1, -1):
                if nums[first_index] < nums[j]:
                    second_index = j
                    break

            # swapping values
            temp = nums[second_index]
            nums[second_index] = nums[first_index]
            nums[first_index] = temp
            
            #reversing values from first_index+1 to lastindex/length of the list/array
            first = first_index + 1
            last = len(nums) - 1
            while first < last:
                temp = nums[last]
                nums[last] = nums[first]
                nums[first] = temp
                first += 1
                last -= 1
            return nums  
        
        
        
        
        
        
     
            
        
        
        
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
