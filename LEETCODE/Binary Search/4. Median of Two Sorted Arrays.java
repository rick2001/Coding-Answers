class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        
        //most-optimized approach
        //lengths
        int n1=nums1.length;  
        int n2=nums2.length;
        if(n1>n2){
            return findMedianSortedArrays(nums2, nums1);   //in this way find the minimum length array in 
        }        
        int n=n1+n2; //total length
        int low=0, high=n1;
        int left=(n1+n2+1)/2;
        
        //binary search
        while(low<=high){
            int mid1=(low+high)/2;  
            int mid2=left-mid1; // if on left side i need 5 elements, so if mid1 is giving 2 elements so mid2 will give total 3 element. thats why simply do left-mid1
            int l1=Integer.MIN_VALUE, l2=Integer.MIN_VALUE;
            int r1=Integer.MAX_VALUE, r2=Integer.MAX_VALUE;
            
            // finding the l1,r1,l2,r2
            if(mid1<n1) r1=nums1[mid1];   //mid1 or mid2 should alwayes be valid index, not any hypothetical index
            if(mid2<n2) r2=nums2[mid2];
            
            if(mid1-1>=0) l1=nums1[mid1-1];
            if(mid2-1>=0) l2=nums2[mid2-1];
            
            // conditions of performingf binary search
            if(l1<=r2 && l2<=r1){
                if(n%2==1) return Math.max(l1,l2);
                else{
                    return (double) (Math.max(l1,l2)+Math.min(r1,r2))/2.0;
                }
            }
            else if(l1>r2){
                high=mid1-1;
            }
            else{
                low=mid1+1;
            }
            
        }
        return 0;
        
        
        
        
        
        //better approach(T.C->O(N), S.C->O(1))
        // length of each array
//         int n1=nums1.length;
//         int n2=nums2.length;
        
//         int n=n1+n2;//total size
        
//         // required indexes
//         int index2=n/2;
//         int index1=index2-1;
//         int count=0;
        
//         int element1=-1, element2=-1;
        
//         //apply merge step
//         int i=0,j=0;
//         while(i<n1 && j<n2){
//             if(nums1[i]<nums2[j]){
//                 if(count==index1) element1= nums1[i];
//                 if(count==index2) element2= nums1[i];
//                 count++;
//                 i++;
//             }
//             else{
//                 if(count==index1) element1= nums2[j];
//                 if(count==index2) element2= nums2[j];
//                 count++;
//                 j++;
//             }
//         }
        
//         while(i<n1){
//             if(count==index1) element1= nums1[i];
//             if(count==index2) element2= nums1[i];
//             count++;
//             i++;
//         }
//         while(j<n2){
//             if(count==index1) element1= nums2[j];
//             if(count==index2) element2= nums2[j];
//             count++;
//             j++;
//         }
        
//         if(n%2!=0){
//             return (double) element2;
//         }
//         return (double) ((double) (element1+element2))/2.0;
        
        
        
        
        
        
        // extreme bruteforce approach(T.C->O(N), S.C->O(N))
//         int n1=nums1.length;
//         int n2=nums2.length;
//         List<Integer> nums3=new ArrayList();
//         int i=0,j=0;
//         while(i<n1 && j<n2){
//             if(nums1[i]<=nums2[j]){
//                 nums3.add(nums1[i]);
//                 i++;
//             }
//             else{
//                 nums3.add(nums2[j]);
//                 j++;
//             }
//         }
//         while(i<n1){
//             nums3.add(nums1[i]);
//             i++;
//         }
        
//         while(j<n2){
//             nums3.add(nums2[j]);
//             j++;
//         }
//         int n=n1+n2;
        
//         if(n%2!=0){
//             return (double) (nums3.get(n/2));
//         }
//         return (double) ((double) nums3.get(n/2) + (double) nums3.get(n/2-1))/2.0;
        
    }
}
