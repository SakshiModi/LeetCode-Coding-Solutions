class Solution:
    def removeDuplicates(self, nums):
        count=0
        for i in range(1,len(nums)):
            if(nums[count]!=nums[i]):
                count=count+1
                nums[count]=nums[i]
        return count+1
        