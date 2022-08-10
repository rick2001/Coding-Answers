#User function Template for python3

# function should return a triplet
# if no such triplet is found return
# a container results as empty
def findTriplet(arr,n):
    # a+b=c
    # so we can say a=c-b
    # solved by riju
    # z = []
    # for j in range(len(arr)):
    #     required = {}
    #     for i in range(len(arr)):
    #         if arr[j] - arr[i] in required:
    #             return [1,2,3]
    #         else:
    #             required[arr[i]]=i
    # return (z)
    
    
    #tried by me
    # arr.sort()
    # for i in range(len(arr)-2):
    #     val = arr[i]
    #     low=i+1
    #     high=n-1
    #     while low<=high:
    #         if arr[high]-arr[low]==val:
    #             return [arr[low],arr[high],val]
    #         elif arr[high]-arr[low] < val:
    #             low+=1
    #         else:
    #             high-=1
    # return []
    
    #we know a+b=c
    arr.sort()
    for i in range(len(arr)-1,-1,-1):
        val=arr[i]
        low=0
        high=i-1
        while low<high:
            if arr[low]+arr[high]==val:
                return [arr[low],arr[high],val]
            elif arr[low]+arr[high] <val:
                low+=1
            else:
                high-=1
    return []
    
    
    
    
    
    # for i in range(len(arr)):
    #     for j in range(i+1,len(arr)):
    #         for k in range(j+1,len(arr)):
    #             sum = arr[i]+arr[j]
    #             if sum == k:
    #                 return [arr[i],arr[j],sum]
    # return []
