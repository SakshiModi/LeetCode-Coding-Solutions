class Solution:
    def maxSubArray(self, nums):
        n=len(nums)
        sum=nums[0]
        maxSum=sum
        for i in range(1,n):
            if((sum+nums[i])>=nums[i]):
                sum=sum+nums[i]
            else:
                sum=nums[i]
            if(maxSum<sum):
                maxSum=sum
        return maxSum
        