class Solution {
    public int singleNonDuplicate(int[] nums) {
        // using the optimal approach (Binary Search)
        
        int low=0; 
        int high=nums.length-2;
        while(low<=high){
            int mid=(low+high)/2;
            if(nums[mid]==nums[mid^1]) low=mid+1;
            else high=mid-1;
        }
        return nums[low];
        
        
        
        
        // using xor concept (T.C-> O(N) and S.C-> O(1))
        // int result=0;
        // for(int i=0; i<nums.length; i++){
        //     result=result^nums[i];
        // }
        // return result;
        
        
        
        
        // my own written solution
//         if(nums.length==1){
//             return 1;
//         }
//         int start=0;
//         int val=-1;
//         while(start<nums.length-1){
//             if(nums[start]==nums[start+1]){
//                 start+=2;
//             }
//             else{
//                 val=nums[start];
//                 break;
//             }
            
//         }
//         if(val==-1){
//             return nums[nums.length-1];
//         }
//         return val;
    }
}
