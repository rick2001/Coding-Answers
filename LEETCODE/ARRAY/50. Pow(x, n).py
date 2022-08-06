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
        
