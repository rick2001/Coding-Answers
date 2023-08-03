# simple solution with T.C-> O(N)+O(N^2) and S.C-> O(1)

class Solution(object):
    def sumi(self, val):
        add=0
        while val!=0:
            rem=val%10
            add+=rem
            val=val//10
        return add
    
    
    def getLucky(self, s, k):
        val=""
        for i in s:
            index=ord(i)
            temp=96
            if(index>=97 and index<=122):
                difference=index-temp
                val+=str(difference)
        result=int(val)
        for i in range(k):
            result=self.sumi(result)
        return result
