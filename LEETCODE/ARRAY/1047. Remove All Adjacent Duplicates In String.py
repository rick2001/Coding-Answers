class Solution(object):
    def removeDuplicates(self, s):
        newstring=""    # where we will store the new string
        stack=[]     # will perform stack operation
        top=-1
        for i in range(len(s)):
            if top==-1:
                stack.append(s[i])
                top+=1
            else:
                if stack[top]==s[i]:
                    stack.pop(top)
                    top-=1
                else:
                    stack.append(s[i])
                    top+=1
                    
        for val in stack:    #concatinating all the values to newstring   
            newstring+=val
        return newstring
            
            
            
            
            
        """
        :type s: str
        :rtype: str
        """
        
