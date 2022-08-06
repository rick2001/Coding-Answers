class Solution {
    public List<Integer> majorityElement(int[] nums) {
        // if (nums.length == 1){
        //     return nums;
        // }
        int elm1,elm2;
        int count1,count2;
        elm1=-2;  //assuming it as -1 because in test cases -1 is present otherwise we can consider it as -1 or None in other language
        elm2=-2;
        count1=0;
        count2=0;
        
        for(int val:nums){
            if(val==elm1){
                count1+=1;
            }
            else if(val==elm2){
                count2+=1;
            }
            else if(count1==0){
                elm1=val;
                count1=1;
            }
            else if(count2==0){
                elm2=val;
                count2=1;
            }
            else{
                count1--;
                count2--;
            }
        }
        // System.out.println(elm1);
        // System.out.println(elm2);
        ArrayList<Integer> array = new ArrayList<Integer>();
        count1=0;
        count2=0;
        for (int val: nums){
            if(val==elm1){
                count1++;
            }
            if(val==elm2){
                count2++;
            }
        }
        int check = nums.length/3;
        if (count1 > check){
            array.add(elm1);
        }
        if (count2 > check){
            array.add(elm2);
        }
        return array;
        
    }
}
