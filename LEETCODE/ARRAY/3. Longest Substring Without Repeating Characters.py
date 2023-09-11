class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left=0, right=0;
        int maximum=0;
        Map<Character, Integer> hashMap=new HashMap<>();
        while(right<s.length()){
            if(hashMap.containsKey(s.charAt(right))){
                left=Math.max(hashMap.get(s.charAt(right))+1, left);
            }
            hashMap.put(s.charAt(right), right);
            maximum=Math.max(maximum, right-left+1);
            right++;
        }
        return maximum;
    }
}



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
        
        #Optimized (Python)
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

#Optimized (Java)
        # T.C-> O(2N)
        # S.C-> O(N)
# class Solution {
#     public int lengthOfLongestSubstring(String s) {
#         int left=0, right=0; 
#         int maximum=0;
#         Set<Character> hashSet=new HashSet<>();
#         while(right<s.length()){
#             if(hashSet.contains(s.charAt(right))){
#                 while(left<right && hashSet.contains(s.charAt(right))){
#                     hashSet.remove(s.charAt(left));
#                     left++;
#                 }
#                 hashSet.add(s.charAt(right));
#             }
#             else{
#                 hashSet.add(s.charAt(right));
#                 maximum=Math.max(maximum, right-left+1);
#             }
#             right++;
#         }
#         return maximum;
        
#     }
# }
