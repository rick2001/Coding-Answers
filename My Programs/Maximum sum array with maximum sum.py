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
