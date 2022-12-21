#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
	    def answer(index, final_arr, count, arr, N):
            if index == N:
                final_arr.append(count)
                return
            count+=arr[index]
            answer(index+1, final_arr, count, arr, N)
            count-=arr[index]
            answer(index+1, final_arr, count, arr, N)
        
        index=0
        final_arr=[]
        count=0
        answer(index, final_arr, count, arr, N)
        return final_arr
