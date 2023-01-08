class Solution:
#     Most Optimized Approach
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def answer(index, candidates, target, empty_arr ,final_arr):
            if target ==0:
                final_arr.append(empty_arr.copy())
                return
            
            for i in range(index,len(candidates)):
                if i>index and candidates[i]==candidates[i-1]: #candidates[i]==candidates[i-1-> this portion is mainly to avoid duplicates for different different 
                    continue
                if candidates[i] > target:
                    break
                    
                empty_arr.append(candidates[i])
                answer(i+1, candidates, target-candidates[i], empty_arr ,final_arr)
                empty_arr.pop()
        
        index=0
        candidates.sort()
        empty_arr=[]
        final_arr=[]
        answer(index, candidates, target, empty_arr ,final_arr)
        return final_arr
        
        
