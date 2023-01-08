class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def answer(index, target, candidates, empty_array, final_array):
            
            if index==len(candidates):
                if target == 0:
                    final_array.append(empty_array.copy())
                return

            if candidates[index] <= target:

                empty_array.append(candidates[index])
                answer(index, target-candidates[index], candidates, empty_array, final_array)
                empty_array.pop()
            answer(index+1, target, candidates, empty_array, final_array)
        
        
        index=0
        final_array=[]  #final array where all the combinations will be stored
        empty_array=[]  #we will use it to find the combinations
        answer(index, target, candidates, empty_array, final_array)
        return final_array
        
