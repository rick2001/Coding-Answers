class Solution:
    def findTwoElement( self,arr, n): 
        store1=0
        store2=0
        emp = [0]*(n+1)
        for i in range(n):
            emp[arr[i]]+=1
        for j in range(1,n+1):
            if emp[j] == 0:
                store1 = j
            if emp[j] > 1:
                store2= j
        return store2, store1
        # code here
