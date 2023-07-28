class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        #base cases
        if len(nums1)==0 and len(nums2)==0:
            return None
        if len(nums1)==0 and len(nums2)!=0:
            return nums2
        if len(nums1)!=0 and len(nums2)==0:
            return nums1
        
        
        ansArray=[]  #answer array
        i=0;
        j=0;
        
        while i<len(nums1) and j<len(nums2):
            if(nums1[i][0]==nums2[j][0]):     #checking if both array 0th index is same so simply perform addition as per instruction and add it into the answer array
                val=nums1[i][1]+nums2[j][1]
                ansArray.append([nums1[i][0], val])
                i+=1
                j+=1
            else:               #Condition:  if the 0th indexes are not same
                if nums1[i][0]< nums2[j][0]:  #checking the num1 and num2 0th index. whichever is lesser add it into the answer array 
                    ansArray.append(nums1[i])
                    i+=1
                else:                        
                    ansArray.append(nums2[j])
                    j+=1
        
        if(i < len(nums1)):   #checking if any values are left so simply add those in the answer array
            for val in range(i, len(nums1)):
                ansArray.append(nums1[val])
        if(j < len(nums2)):    #checking if any values are left so simply add those in the answer array
            for val in range(j, len(nums2)):
                ansArray.append(nums2[val])
                
                
        return ansArray   #returning the answer array
                
        
