class Solution(object):
    def uniquePaths(self, m, n):
        #Using combination method
        N=m+n-2
        R=m-1
        res = 1
        for i in range(1,R+1):
            res=(res*(N-R+i))//i
        return 
