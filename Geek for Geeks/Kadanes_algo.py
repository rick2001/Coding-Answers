class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        sum=0
        maxinum =arr[0]
        for i in range(N):
            sum =sum + arr[i]
            if sum > maxinum:
                maxinum = sum
            if sum<0:
                sum=0
        return maxinum
