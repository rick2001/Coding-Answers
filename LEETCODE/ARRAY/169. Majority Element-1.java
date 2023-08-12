// code is available in both Java and python
// T.C-> O(N)+O(N) S.C-> O(1)

//JAVA
class Solution {
    public int majorityElement(int[] nums) {
        int count=0;
        int element=0;
        for(int val:nums){
            if(count==0){ 
                count=1;
                element=val;
            }
            else if(element==val) count++;
            else count--;
        }
        int count1=0;
        for(int val: nums){
            if(val==element) count1++;
        }
        if(count1 > nums.length/2) return element;
        else return -1;
        
        
        
        
        
        
        // brute force approach
    //     Map<Integer, Integer> hashMap=new HashMap<>();
    //     for(int val:nums){
    //         if(hashMap.containsKey(val)){
    //             hashMap.put(val, hashMap.get(val)+1);
    //         }
    //         else{
    //             hashMap.put(val,1);
    //         }
    //     }
    //     System.out.print(hashMap);
    //     int maxValue=Integer.MIN_VALUE;
    //     int maxKey=0;
    //     for(Integer key:hashMap.keySet()){
    //         if(hashMap.get(key)>maxValue){
    //             maxValue=hashMap.get(key);
    //             maxKey=key;
    //         }
    //     }
    //     return maxKey;
    // }
// }

// Python
class Solution(object):
    def majorityElement(self, nums):
        # Using Moores voting algorithm
        count =0
        element=0
        
        for val in nums:
            if count==0:
                element = val
            if element == val:
                count+=1
            else:
                count-=1
        count1=0
        for value in nums:
            if value==element: count1+=1
        if(count1> len(nums)//2): return element 
        else: return -1
        
        
        
        
        
        
        
        
        // #Better Approach
        // #Using hashmap T.C=> O(logn) for using hashmap and space comp=> O(N)
        // # hashmap={}
        // # for i in nums:
        // #     # count=1
        // #     if i in hashmap:
        // #         hashmap[i]+=1
        // #     else:
        // #         hashmap[i]=1
        // # maximum = max(hashmap, key=lambda x: hashmap[x])
        // # # print(maximum)
        // # return maximum
        
        
        
        
        """
        :type nums: List[int]
        :rtype: int
        """
        

    
