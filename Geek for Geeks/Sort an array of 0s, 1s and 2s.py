class Solution:
    def sort012(self,arr,n):
        mid = left = 0
        high = n-1
        # for i in range(1,n):
        while(mid <= high):
            
            if arr[mid] == 0:
                temp=arr[mid]
                arr[mid] = arr[left]
                arr[left] = temp
                # high-=1
                left+=1
                mid+=1
            elif arr[mid]==1:
                mid+=1
            elif arr[mid]==2:
                temp=arr[mid]
                arr[mid] = arr[high]
                arr[high] = temp
                high-=1
        return arr
                
