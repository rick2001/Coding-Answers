class Solution(object):
    def longestConsecutive(self, nums):
        #bruteforce solution
#         if len(nums)==0:
#             return 0
#         nums=list(set(nums))    #here if same value is repeted then we will consider only the unique values
#         nums.sort()
#         # store=nums[0]
#         current=answer=1
            
#         for i in range(1,len(nums)):
#             if (nums[i]-nums[i-1])==1: #if the difference between the number and its previous number is 1, that means it is consiquitive/continious
#                 current+=1
#             elif (nums[i]-nums[i-1])!=1:
#                 current=1
#             answer=max(answer,current)
#         return answer

#       optimal solution
        hashSet=set(nums)
        longest=0
        for val in nums:
            if (val-1) not in hashSet:
                length=0
                while(val+length) in hashSet:
                    length=length+1
                longest=max(longest,length)
        return longest
