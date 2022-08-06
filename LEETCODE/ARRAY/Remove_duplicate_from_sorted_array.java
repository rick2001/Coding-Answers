class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 1){
            return 1;
        }
        else{
            int i=0;
            int j=1;
            while (j < nums.length){
                if(nums[i] == nums[j]){
                    j+=1;
                }
                else{
                    i++;
                    nums[i]=nums[j];
                    j++;
                }
                
            }
            return i+1;
        }
        
    }
}
