class Solution(object):
    def merge(self, nums1, m, nums2, n):
        #bruteforce solution
        # last = m+n-1
        # while n>0:
        #     nums1[last] = nums2[n-1]
        #     last-=1
        #     n-=1
        # nums1.sort()
        
        #optimal solution
        
        # m is index of num1. upto m index the values of num1 array will be considered 
        # n is length of the num2 array
        # lastindex of m
        lastindex = m+n-1
        
        while m>0 and n>0:
            if nums1[m-1] > nums2[n-1]:
                
                nums1[lastindex] = nums1[m-1]
                m=m-1
            else:
                nums1[lastindex] = nums2[n-1]
                n=n-1
            lastindex-=1
        while n>0:
            nums1[lastindex] = nums2[n-1]
            lastindex-=1
            n-=1
