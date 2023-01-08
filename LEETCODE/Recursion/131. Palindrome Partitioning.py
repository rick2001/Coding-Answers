class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        
        def answer(index, emp_arr, final_arr, s):
            if index == len(s):
                final_arr.append(emp_arr.copy())
                return
            
            for i in range(index,len(s)):
                if ispalindrome(index, i, s):
                    emp_arr.append(s[index:i+1])
                    answer(i+1, emp_arr, final_arr, s)
                    emp_arr.pop()
                    
        def ispalindrome(start, end, string):
            while start <= end:
                if string[start] != string[end]:
                    return False
                start+=1
                end-=1
            return True
        
        
        
        index=0
        emp_arr=[]
        final_arr=[]
        answer(index, emp_arr, final_arr, s)
        return final_arr
        
