class Solution(object):
    def twoSum(self, numbers, target):
        # #T.C-> O(N)
        hashmap={}
        for i in range(len(numbers)):
            val=target-numbers[i]
            if val in hashmap:
                return [hashmap[val],i+1]
            else:
                hashmap[numbers[i]]=i+1
        
        
        #another solution
        # a+b=k
        # b=k-a
        #bruteforce
        # for i in range(len(numbers)-1):
        #     val=target-numbers[i]
        #     for j in range(i+1,len(numbers)):
        #         if numbers[j]==val:
        #             return [i+1,j+1]
        
        
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
