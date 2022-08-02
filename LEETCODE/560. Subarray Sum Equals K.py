class Solution(object):
    def subarraySum(self, nums, k):
        sumi=0
        hashmap={}
        count=0
        
        for i in range(len(nums)):
            sumi+=nums[i]
            if sumi == k:
                count+=1
            if (sumi-k) in hashmap:
                count+=hashmap[sumi-k]
            
            if sumi not in hashmap:
                hashmap[sumi]=1
            else:
                hashmap[sumi]+=1
        return count
    
    #Bruteforce
    # count=0
    #     for i in range(len(nums)):
    #         sumi=0
    #         for j in range(i,len(nums)):
    #             sumi+=nums[j]
    #             if sumi == k:
    #                 count+=1
    #     return count
                
        
        
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
