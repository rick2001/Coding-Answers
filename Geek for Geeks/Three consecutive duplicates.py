class Solution:
	def remove3ConsecutiveDuplicates(self, S):
	    
	    stack=[]    #defining the stack
        top=-1
        newstring=""      #declaring the empty string where we will store the new string and we will return
        if len(S)==1:
            return S
        
        for i in range(len(S)):
            if top==-1 or top==0:
                stack.append(S[i])
                top+=1
            
            else:
                if S[i]==stack[top] and S[i]==stack[top-1]:
                    stack.pop(top)
                    top-=1
                    stack.pop(top)
                    top-=1
                else:
                    
                    stack.append(S[i]) 
                    top+=1          
        for val in stack:
            newstring+=val
        return -1 if len(newstring)==0 else newstring
