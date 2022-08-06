class Solution {
    public int majorityElement(int[] nums) {
        int count =0;
        int element = 0;
        
        for (int val:nums){
            if (count == 0){
                element = val;
            }
            if (element == val){
                count+=1;
            }
            else{
                count-=1;
            }
        }
        return element;
        
    }
}
