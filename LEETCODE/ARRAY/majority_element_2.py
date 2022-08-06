class Solution(object):
    def majorityElement(self, nums):
        if len(nums)==1:
            return nums
        element1,element2= None, None
        count1,count2 = 0,0
        
        # here we will find the majority 2 elements which has highest frequency
        for val in nums:
            if val == element1:
                count1+=1
            elif val == element2:
                count2+=1
            elif count1==0:
                element1=val
                count1=1
            elif count2==0:
                element2=val
                count2=1
            else:
                count1-=1
                count2-=1
        # Now here we will check weather both the element frequency is greater than n/3 or not
        # If yes then add it in the list and return it else add the only element in the list and return it.
        array=[]
        count1,count2=0,0
        for val in nums:
            if element1==val:
                count1+=1
            if element2==val:
                count2+=1
        if count1 > len(nums)//3:
            array.append(element1)
        if count2 > len(nums)//3:
            array.append(element2)
        return array
        
            
        
        
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
