# code is available in both java and python
# JAVA
class Solution {
    public double myPow(double x, int n) {
        if(x==0) return 0;
        if(n==0) return 1;
        double ans=1.0;
        long nn=n;  //taking it long as temp variable because if n is negative (The range is -2,147,483,647), positive conversion of n cant be stored in int type.
        if(n<0) nn=-1 * nn;  // convert it into positive value
        
        while(nn > 0){
            if(nn%2==0){   // if n is even number
                x=x*x;
                nn= nn/2;
            }
            else{          // if n is odd number
                ans=ans*x;
                nn=nn-1;
            }
        }
        if(n<0) ans= (double)1.0/(double)ans;   //id n is negative then perform 1/x^n;
        return ans;
            
        
    }
}


# PYTHON
class Solution(object):
    def myPow(self, x, n):
        #basic solution
        # v="{:.5f}".format(x**n)
        # return float(v)
        
        def finding(x,n):
            if x==0: return 0
            if n==0: return 1
            
            result = finding(x,n//2)
            result = result*result
            return result*x if n%2 else result
        result =  finding(x,abs(n))
        
        return result if n>=0 else 1/result
            
            
        
        
        
        
        
        
        
        
        
        
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
