// both java and python code are available
//java
public class Solution {
    public int countDigits(int num) {
        int count = 0;
        String numStr = Integer.toString(num);
        for (char val : numStr.toCharArray()) {
            // here i am using STring.ValueOf() function to convert the value into string as because Integer.parseInt() can convert a string into integer only not a character
            int digit = Integer.parseInt(String.valueOf(val));   // or i can use
            // int digit=Character.getNumericValue(val);
            if (num % digit == 0) {
                count++;
            }
        }
        return count;
    }
}


//python

class Solution(object):
    def countDigits(self, num):
        count=0
        for val in str(num):
            if(num%int(val)==0):
                count+=1
        return count
            
        
        
        """
        :type num: int
        :rtype: int
        """
        
