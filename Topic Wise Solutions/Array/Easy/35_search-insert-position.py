class Solution:
    def searchInsert(self, nums, target):
        ans=len(nums)
        for i in range(len(nums)):
            if(target<=nums[i]):
                ans=i
                break
        return ans
                