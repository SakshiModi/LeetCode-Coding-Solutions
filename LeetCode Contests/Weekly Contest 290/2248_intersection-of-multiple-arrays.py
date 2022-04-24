class Solution:
    def intersection(self, nums):
        n=len(nums)
        ans=set(nums[0])
        for i in range(1,n):
            ans=ans.intersection(set(nums[i]))
        return sorted(list(ans))