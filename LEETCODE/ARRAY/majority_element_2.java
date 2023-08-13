// code is available in both java and python
// JAVA
class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int count1=0;
        int count2=0;
        
        int elem1=Integer.MIN_VALUE;
        int elem2=Integer.MIN_VALUE;
        List<Integer> output=new ArrayList<>();
        
        for(int i=0; i<nums.length; i++){
            if(count1==0 && nums[i]!=elem2){
                elem1=nums[i];
                count1=1;
            }
            else if(count2==0  && nums[i]!=elem1){
                elem2=nums[i];
                count2=1;
            }
            else if(elem1==nums[i] ){
                count1++;
            }
            else if(elem2==nums[i]){
                count2++;
            }
            else{
                count1--;
                count2--;
            }
        }
        int latCount1=0;
        int latCount2=0;
        for(int i=0; i<nums.length; i++){
            if(elem1==nums[i]){
                latCount1++;
            }
            if(elem2==nums[i]){
                latCount2++;
            }
        }
        if(latCount1 > nums.length/3) output.add(elem1);
        if(latCount2 > nums.length/3) output.add(elem2);
        return output;
        
    }
}


// PYTHON
class Solution(object):
    def majorityElement(self, nums):
        if len(nums)==1:
            return nums
        element1,element2= None, None
        count1,count2 = 0,0
        
        # here we will find the majority 2 elements which has highest frequency
        for val in nums:
            if val == element1:
                count1+=1
            elif val == element2:
                count2+=1
            elif count1==0:
                element1=val
                count1=1
            elif count2==0:
                element2=val
                count2=1
            else:
                count1-=1
                count2-=1
        # Now here we will check weather both the element frequency is greater than n/3 or not
        # If yes then add it in the list and return it else add the only element in the list and return it.
        array=[]
        count1,count2=0,0
        for val in nums:
            if element1==val:
                count1+=1
            if element2==val:
                count2+=1
        if count1 > len(nums)//3:
            array.append(element1)
        if count2 > len(nums)//3:
            array.append(element2)
        return array
        
            
        
        
        
