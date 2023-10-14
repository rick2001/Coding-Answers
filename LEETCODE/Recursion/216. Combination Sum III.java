class Solution {
    public void answer(int index, int k, int target, int sum, List<Integer> temp, List<List<Integer>> result){
        if(temp.size()==k){  // doing it as per the condition
            if(sum==target){
                result.add(new ArrayList<>(temp));
            }
            return;
        }
        for(int i=index; i<=9; i++){   //as per the condition running it from 0 to 9
            if(i > target){
                break;
            }
            sum+=i;
            temp.add(i);
            answer(i+1, k, target, sum, temp, result);
            sum-=i;
            temp.remove(temp.size()-1);
            
        }
    }
    public List<List<Integer>> combinationSum3(int k, int n) { // n is the expected sum, and k is the valid combination of k numbers.
        List<List<Integer>> result=new ArrayList<>();
        List<Integer> temp=new ArrayList<>();
        int sum=0;
        answer(1, k, n, sum, temp, result);
        return result;
    }
}
