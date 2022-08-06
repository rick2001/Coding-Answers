class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        # A-> it is the array
        # B-> It is the target 
        
        xor=0
        count=0
        hashmap={}
        for i in range(len(A)):
            xor^=A[i]
            if xor == B:
                count+=1
                
            if (xor^B) in hashmap:
                count+=hashmap[xor^B]
            
            if xor not in hashmap:
                hashmap[xor]=1
            else:
                hashmap[xor]+=1
        return count
