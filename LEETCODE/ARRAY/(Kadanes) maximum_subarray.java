class Solution {
    public int maxSubArray(int[] nums) { 
        if (nums.length == 1){
            return nums[0];
        }
        else{
            int sum=0;
            int maximum = nums[0];
            for (int number: nums){
                sum+=number;
                if (sum>maximum){
                    maximum=sum;
                }
                if (sum < 0){
                    sum=0;
                }
            }
            return maximum;
        }
    }
}
