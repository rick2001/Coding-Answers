class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        
        
        # T.C-> O(2NlogN) + O(2N)
        # S.C-> O(1)
        
        
        arr.sort()
        dep.sort()
        
        platform_needed=1
        max_platform_needed = 1
        i=1
        j=0
        
        while i<len(arr) and j<len(dep):
            if arr[i] <= dep[j]:
                platform_needed+=1
                i+=1
            elif dep[j] < arr[i]:
                platform_needed-=1
                j+=1
            
            max_platform_needed = max(max_platform_needed, platform_needed)
        return max_platform_needed
