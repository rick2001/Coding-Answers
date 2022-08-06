#User function Template for python3

class Solution:
    def removeConsecutiveCharacter(self, S):
        
        # code here
        
        stack=[]    #defining the stack
        top=-1
        newstring=""      #declaring the empty string where we will store the new string and we will return
        if len(S)==1:
            return S
        
        for i in range(len(S)):
            if top==-1:
                stack.append(S[i])
                top+=1
            
            else:
                if S[i]==stack[top]:
                    stack.pop(top)
                    top-=1
                
                
                stack.append(S[i])   #Here the reason why we didnot use else because after if condition also we have to use this 
                top+=1          #block. if we dry run it we will understand it better
        for val in stack:
            newstring+=val
        return newstring
                    
