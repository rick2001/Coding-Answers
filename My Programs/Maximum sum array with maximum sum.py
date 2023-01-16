# -> print the maximum subarray sum along with the subarray.

# Most Optimized (extension of the Kadanes Algorithm)
def maxSubArray(nums):
    sumi = 0
    maxi = -1
    start=None
    end=None
    new=[]
    for i in range(len(nums)):
        sumi += nums[i]
        if sumi > maxi:
            maxi = sumi
            if start==None and end==None:
                start=i
                end=i
            else:
                end=i
        if sumi < 0:
            sumi = 0
            start=None
            end=None
    for j in range(start,end+1):
        new.append(nums[j])
    print(f"maximum sum is->{maxi}")
    print(f"maximum array is->{new}")
# nums=[-2,1,-3,4,-1,2,1,-5,4]
# nums=[1,2,7,-4,3,2,-10,9,1]
nums=[10,20,-30,40,-50,60]
maxSubArray(nums)




# BruteForce Approach
# T.C-> O(N^2)
# S.C-> O(1)
def solution(nums):
    maxi=nums[0]
    start=None
    end=None
    newarr=[]
    for i in range(len(nums)):
        sumi=0
        for j in range(i,len(nums)):
            sumi+=nums[j]
            if sumi > maxi:
                maxi=sumi
                start=i
                end=j
    for k in range(start,end+1):
        newarr.append(nums[k])
    print("Maximum Sum is-> ",maxi)
    print("The Array is-> ",newarr)
# nums=[-2,1,-3,4,-1,2,1,-5,4]
nums=[5,4,-1,7,8]
solution(nums)
