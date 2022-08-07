class Solution:
    def countElements(self, nums):
        minElem=min(nums)
        maxElem=max(nums)
        count=0
        for i in range(len(nums)):
            if nums[i]==minElem or nums[i]==maxElem:
                pass
            else:
                count+=1
        return count