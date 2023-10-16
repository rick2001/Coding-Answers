// Java
class Solution {
    public boolean isPalindrome(String val, int start, int end){
        while(start<=end){
            if(val.charAt(start++)!=val.charAt(end--)) return false;
        }
        return true;
    }
    
    public void answer(int index, String s, List<String> temp, List<List<String>> result){
        if(index==s.length()){
            result.add(new ArrayList<>(temp));
            return;
        }
        
        for(int i=index; i<s.length(); i++){
            if(isPalindrome(s, index, i)){
                temp.add(s.substring(index, i+1));
                answer(i+1, s, temp, result);
                temp.remove(temp.size()-1);
            }
        }
    }
    
    public List<List<String>> partition(String s) {
        List<List<String>> result=new ArrayList<>();
        List<String> temp=new ArrayList<>();
        answer(0, s, temp, result);
        return result;
        
    }
}


// python
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
        
