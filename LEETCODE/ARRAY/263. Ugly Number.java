import java.util.*;
class Solution{
    public boolean isUgly(int n){
        if(n<=0){
            return false;
        }
        if(n==1){
            return true;
        }
        int array[] = {2,3,5};
        // System.out.println(array);
        for(int val:array){
            while(n%val==0){
                n=n/val;
            }
        }
        return n==1;  //if the value remains 1 then it is true else it is false
        
    }
}

// //simple bruteforce solution
// class Solution {
//     public boolean isUgly(int n) {
//         if(n<=0){
//             return false;
//         }
//         if(n==1){
//             return true;
//         }
//         for(int div=2; div<n; div++){
//             if(div>5){
//                 return false;
//             }
//             while(n%div==0){
//                 n=n/div;
//             }
//         }
//         return true;
//     }
// }
