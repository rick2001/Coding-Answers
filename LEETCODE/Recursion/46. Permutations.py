class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # T.C-> O(N!*N)
        # S.C-> O(N!) + O(N) + O(N) + O(N)
        # Approach-1 recursive solution
#         def answer(nums, empty_arr, final_arr, map_arr):
            
#             if len(empty_arr) == len(nums):
#                 final_arr.append(empty_arr.copy())
#                 return
            
#             for i in range(len(nums)):
#                 if map_arr[i]==0:
#                     map_arr[i] = 1
#                     empty_arr.append(nums[i])
#                     answer(nums, empty_arr, final_arr, map_arr)
#                     map_arr[i] = 0
#                     empty_arr.pop()
        
        
#         empty_arr=[]
#         final_arr=[]
#         map_arr=[0]*len(nums)
#         answer(nums, empty_arr, final_arr, map_arr)
#         return final_arr
    
    
        # Approach-2 recursive solution
        #T.C-> O(N!*N)
        #S.C-> O(N!) + O(N)
        # Takes less Space as compared to Approch-1
        def answer(index, final_arr, nums):
            
            if index == len(nums):
                final_arr.append(nums.copy())
                return
            
            for i in range(index, len(nums)):
                temp1 = nums[i]
                nums[i] = nums[index]
                nums[index] = temp1
                
                answer(index+1, final_arr, nums)
                
                temp2 = nums[i]
                nums[i] = nums[index]
                nums[index] = temp2
                
        
        
        index=0
        final_arr=[]
        answer(index,final_arr,nums)
        return final_arr
    
        
