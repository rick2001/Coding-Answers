class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Most Optimized Approach O(2^n * n) ->T.C
        # S.C-> O(2^n) * O(n) 
        
        if len(nums)==0:
            return nums
        def answer(index, empty_arr, final_arr, nums):
            final_arr.append(empty_arr.copy())
            for i in range(index,len(nums)):
                if i>index and nums[i]==nums[i-1]:
                    continue
                empty_arr.append(nums[i])
                answer(i+1, empty_arr, final_arr, nums)
                empty_arr.pop()
                
        index = 0
        empty_arr=[]
        final_arr=[]
        nums.sort()
        answer(index, empty_arr, final_arr, nums)
        return final_arr
        
        
        
        
        
        # bruteforce approach (Set is used to filter the duplicates)
#         def answer(index, empty_arr, final_arr, nums):
#             if index == len(nums):
#                 if empty_arr not in final_arr:
#                     final_arr.append(empty_arr.copy())
#                 return
            
#             empty_arr.append(nums[index])
#             answer(index+1, empty_arr, final_arr, nums)
            
#             empty_arr.pop()
#             answer(index+1, empty_arr, final_arr, nums)
            
        # index = 0
        # empty_arr=[]
        # final_arr=[]
        # nums.sort()
        # answer(index, empty_arr, final_arr, nums)
        # return final_arr
