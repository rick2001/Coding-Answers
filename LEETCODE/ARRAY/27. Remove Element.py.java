//java
class Solution {
    public int removeElement(int[] nums, int val) {
        int i=0;
        int j= 0;
        
        while (j < nums.length){
            if (nums[j]==val){
                j++;               
            }
            else{
                nums[i]=nums[j];
                i++;
                j++;
            }
            
        }
        return i;
        
    }
}



//python

class Solution(object):
    def removeElement(self, nums, val):
        count=0
        i=0
        j=0
        
        while j < len(nums):
            if nums[j]==val:
                j+=1
            else:
                nums[i]=nums[j]
                i+=1
                j+=1
                
        return i
