class Solution {
    public void answer(int index, int k, int n, List<Integer> temp, List<List<Integer>> result){
        if(temp.size()==k){
            result.add(new ArrayList<>(temp));
            return;
        }
        
        if(index>n){
            return;
        }
        
        
        for(int i=index; i<=n; i++){
            temp.add(i);
            answer(i+1, k, n, temp, result);
            temp.remove(temp.size()-1);
            
        }
    }
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> result=new ArrayList<>();
        List<Integer> temp=new ArrayList<>();
        answer(1, k, n, temp, result);
        return result;
    }
}
