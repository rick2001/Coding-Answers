// this is basically a cycle finding questions. here i can use the same concept which i used in "LinkedList Cycle" Question.
// solution-2
class Solution {
    public int sumOfSquars(int n){
         int squareVal=0;
        while(n!=0){
            int num=n%10;
            squareVal+=(int)Math.pow(num,2);
            n=n/10;
        }
        return squareVal;
    }
    
    
     public boolean isHappy(int n) {
         
         if(n<0){
            return false;
         }
         if(n==1){
            return true;
         }
         int slow=n;
         int fast=n;
         
         do{
             slow=sumOfSquars(slow);
             fast=sumOfSquars(sumOfSquars(fast));
             // if(slow==fast){
             //     return true;
             // }
             
             
         }while(slow!=fast);
         return slow==1;
         
            
         
        
    }
}



// solution-1
// class Solution {
//     public int sumOfSquars(int n){
//         int squareVal=0;
//         while(n!=0){
//             int num=n%10;
//             squareVal+=(int)Math.pow(num,2);
//             n=n/10;
//         }
//         return squareVal;
//     }
    
    
    
//     public boolean isHappy(int n) {
//         if(n<0){
//             return false;
//         }
//         if(n==1){
//             return true;
//         }
        
//         Set<Integer> store=new HashSet<>();
//         while(!store.contains(n)){    // it is similiar to while n not in hashSet.
//             store.add(n);
//             n=sumOfSquars(n);  // it returns the sum of squares of digit.
//             if(n==1){
//                 return true;
//             }
//         }
//         return false;
        
//     }
// }
