class Solution(object):
    def isValid(self, s):
        stack=[]
        top=-1
        for i in range(len(s)):
            if s[i]=="(" or s[i]=="{" or s[i]=="[":     #if opening bracket then simply push it into the stack
                stack.append(s[i])
                top+=1
            else:
                if (top == -1):        # if the stack is empty and the bracket is closing that means it is false
                    return False
                if (s[i]==')' and stack[top]=='(') or (s[i]=='}' and stack[top]=='{') or (s[i]==']' and stack[top]=='['):
                    stack.pop(top)
                    top-=1
                else:
                    return False
        if (top==-1):
            return True
        else:
            return False
        
        
        
        """
        :type s: str
        :rtype: bool
        """
        
