class Solution:
    def twoSum(self, nums, target):
        for i in range(0,len(nums)):
            if (target-nums[i]) in nums[(i+1):len(nums)]:
                lst=[i,(nums[(i+1):len(nums)].index(target-nums[i])+i+1)]
        return lst