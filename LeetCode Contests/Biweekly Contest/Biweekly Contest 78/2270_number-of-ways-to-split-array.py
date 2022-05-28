class Solution:
    def waysToSplitArray(self, nums):
        i=1
        n=len(nums)
        ans=0
        sum_a=nums[0]
        sum_b=sum(nums[1:])
        if sum_a>=sum_b:
            ans+=1
        while(i<n-1):
            sum_a+=nums[i]
            sum_b-=nums[i]
            if sum_a>=sum_b:
                ans+=1
            i+=1
        return ans