class Solution(object):
    def frequencySort(self, nums):
        c = Counter(nums)
        nums.sort(reverse=True)
        nums.sort(key=lambda x: c[x])
        return nums
