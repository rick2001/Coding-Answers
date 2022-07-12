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
        return element
        
        
        
        
        
        
        
        
        #Better Approach
        #Using hashmap T.C=> O(logn) for using hashmap and space comp=> O(N)
        # hashmap={}
        # for i in nums:
        #     # count=1
        #     if i in hashmap:
        #         hashmap[i]+=1
        #     else:
        #         hashmap[i]=1
        # maximum = max(hashmap, key=lambda x: hashmap[x])
        # # print(maximum)
        # return maximum
