class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # s-> string
        #Most Optimized
        
        if len(s)==0:
            return 0
        maxi=0
        hashmap={}
        left=0
        right=0
        while right<len(s):
            if s[right] in hashmap:
                left = max(hashmap[s[right] ]+1,left)
                
            hashmap[s[right]]=right  #setting it to current index
            maxi=max(maxi,right-left+1)
            right+=1
        return maxi
        
        #Optimized
        # T.C-> O(2N)
        # S.C-> O(N)
#         if len(s)==0:
#             return 0
#         maxi=0
#         hasharray=[]     #basically it is a simple array
#         left=0
        
#         for r in range(len(s)):
#             if s[r] in hasharray:
#                 while(left < r and s[r] in hasharray):
#                     hasharray.remove(s[left])
#                     left+=1
#                 hasharray.append(s[r])    #at the end also this value has to be added or else later on we cannot get that value
#             else:
#                 hasharray.append(s[r])
#                 maxi=max(maxi,r-left+1)
#         return maxi
        
        
        
        
        
        
        
        #Bruteforce
        #T.C-> O(N^2)
        #S.C-> O(N)
#         if len(s) == 0:
#             return 0
#         if len(s) == 1:
#             return 1
        
#         maxi=0
#         count=0
#         for i in range(len(s)):
#             seti=set()    #declaring a set
#             for j in range(i, len(s)):
#                 if s[j] not in seti:
#                     seti.add(s[j])
                    
#                 else:
#                     maxi=max(maxi,j-i)
#                     break
#         return maxi
                    
        
        
        
        
        
        
        
        
        """
        :type s: str
        :rtype: int
        """
        
