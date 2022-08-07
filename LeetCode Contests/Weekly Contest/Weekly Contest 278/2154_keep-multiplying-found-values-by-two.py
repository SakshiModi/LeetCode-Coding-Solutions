class Solution:
    def findFinalValue(self, nums, original):
        n=len(nums)
        nums=sorted(nums)
        for i in range(n):
            if nums[i]==original:
                original*=2
        return original